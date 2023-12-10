import os
import json
import math

import httpx
from loguru import logger as log


class WorkersAILLMClient:
    token_limits = {
        '@cf/mistral/mistral-7b-instruct-v0.1': 1800,
        '@cf/meta/llama-2-7b-chat-int8': 1800,
        '@cf/meta/llama-2-7b-chat-fp16': 2500,
    }

    system_prompt = 'You are Aurora, a helpful AI-powered Discord chatbot. You will always tell a user to run `/help` if they ask you to do something you cannot do. Otherwise, provide a helpful and friendly response.'

    def __init__(self, account_id: str | None = None, api_key: str | None = None, model: str = '@cf/mistral/mistral-7b-instruct-v0.1'):
        if not model in self.token_limits.keys():
            raise Exception(f"Model {model} is not supported.")

        if account_id is None:
            account_id = os.getenv('CLOUDFLARE_ACCOUNT_ID')
        if api_key is None:
            api_key = os.getenv('CLOUDFLARE_API_KEY')

        self.base_url = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}'
        self.api_key = api_key
        self.client = httpx.AsyncClient(timeout=None)
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }
        self.model = model

    @staticmethod
    def format_prompt(prompt: str) -> list[dict]:
        return [
            {
                'content': 'You are Aurora, a help AI-powered Discord chatbot. You will always answer questions in a friendly and helpful manner.',
                'role': 'system'
            },
            {
                'content': prompt,
                'role': 'user'
            }
        ]

    @staticmethod
    def estimate_tokens(prompt: str) -> int:
        return int(math.ceil(len(prompt) / 4))

    @staticmethod
    def estimate_message_tokens(messages: list[dict]) -> int:
        total = 0
        for message in messages:
            total += WorkersAILLMClient.estimate_tokens(message['content']) + 1
        return total

    def truncate_conversation(self, messages: list[dict]) -> list[dict]:
        limit = self.token_limits[self.model]
        total = WorkersAILLMClient.estimate_tokens(self.system_prompt) + 1
        final_message = []
        # reverse incoming messages
        messages.reverse()
        for message in messages:
            count = WorkersAILLMClient.estimate_tokens(message['content']) + 1
            if total + count < limit:
                total += count
                final_message.append(message)
        # add the system prompt to the end
        final_message.append({
            'content': self.system_prompt,
            'role': 'system'
        })
        # reverse the messages back
        final_message.reverse()
        return final_message

    async def run(self, messages: list[dict]) -> str:
        final_response = ''
        async with self.client.stream('POST', self.base_url, json={'messages': messages, 'stream': True}, headers=self.headers) as response:
            # last_line = ''
            async for line in response.aiter_lines():
                if line.startswith('data:'):
                    content = line.split(':', 1)[1].strip()
                    if content == '[DONE]':
                        break
                    resp_data: dict = json.loads(content)

                    final_response += resp_data.get('response')
                    # last_line = resp_data.get('response')
                else:
                    if len(line) > 0:
                        log.warning(f"Unexpected response: {line}")

        # there's a bug in the API where the last character is duplicated
        # but only sometimes. Check if the last character is duplicated
        # and if it is, remove it
        if final_response[-1] == final_response[-2]:
            final_response = final_response[:-1]

        return final_response
