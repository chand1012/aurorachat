from nextcord.iterators import HistoryIterator
from nextcord import Client


from ai.tokens import count_tokens, MAX_TOKENS

SYSTEM_MESSAGE = "You are a helpful assistant. Do not apologize for followup questions, just politely answer the user's question."


async def conversation_handler(bot: Client, message_history: HistoryIterator, prompt: str, model: str, tokens: int) -> list[dict]:
    thread_messages = [{
        'role': 'system',
        'content': SYSTEM_MESSAGE
    }]
    # get previous messages in the thread
    # if it was a user, add { 'role': 'user', 'content': message.content }
    # if it was the bot, add { 'role': 'assistant', 'content': message.content }
    # count the tokens first and check if it is too long
    async for msg in message_history:
        if msg.author == bot.user:
            thread_messages.append(
                {'role': 'assistant', 'content': msg.content})
        else:
            thread_messages.append(
                {'role': 'user', 'content': msg.content})
    thread_messages.reverse()
    messages = [{"role": "user", "content": prompt}]
    for msg in thread_messages:
        msg_tokens = count_tokens(msg['content'])
        if msg_tokens + tokens > MAX_TOKENS[model]:
            break
        messages.append(msg)
        tokens += msg_tokens
    messages.reverse()
    return messages
