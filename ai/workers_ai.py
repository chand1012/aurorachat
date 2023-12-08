import os
import json

import httpx
from loguru import logger as log


class WorkersAILLMClient:
    token_limits = {
        '@cf/mistral/mistral-7b-instruct-v0.1': 1800,
        '@cf/meta/llama-2-7b-chat-int8': 1800,
        '@cf/meta/llama-2-7b-chat-fp16': 2500,
    }

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

    async def run(self, messages: list[dict]) -> str:
        final_response = ''
        async with self.client.stream('POST', self.base_url, json={'messages': messages, 'stream': True}, headers=self.headers) as response:
            last_line = ''
            async for line in response.aiter_lines():
                if line.startswith('data:'):
                    content = line.split(':', 1)[1].strip()
                    if content == '[DONE]':
                        break
                    resp_data: dict = json.loads(content)
                    if resp_data.get('response') != last_line:
                        final_response += resp_data.get('response')
                        last_line = resp_data.get('response')
                else:
                    if len(line) > 0:
                        log.warning(f"Unexpected response: {line}")

        return final_response
