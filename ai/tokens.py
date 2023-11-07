import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

MAX_TOKENS = {
    "gpt-4": 8192,
    "gpt-3.5-turbo": 4096,
}


def count_tokens(text: str):
    return len(enc.encode(text))
