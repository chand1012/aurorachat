from ai.converser import conversation_handler, SYSTEM_MESSAGE
from ai.tokens import count_tokens, MAX_TOKENS
from ai.req import req

CHAT_MODELS = {
    'normal': 'gpt-3.5-turbo',
    'better': 'gpt-3.5-turbo-16k',
    'best': 'gpt-4'
}
