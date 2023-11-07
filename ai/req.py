from openai import OpenAI


def req(o: OpenAI, messages: list[dict]) -> str | list[str]:
    resp = o.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages)
    if len(resp.choices) == 0:
        return "No response"
    return resp.choices[0].message.content
