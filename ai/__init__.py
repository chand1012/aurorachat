from ai.tokens import count_tokens, MAX_TOKENS
from ai.workers_ai import WorkersAILLMClient
CHAT_MODELS = {
    'normal': 'gpt-3.5-turbo',
    'better': 'gpt-3.5-turbo-16k',
    'best': 'gpt-4'
}

IMAGE_MODELS = {
    'normal': 'dall-e-2',
    'better': 'sdxl',
    'best': 'dall-e-3'
}
