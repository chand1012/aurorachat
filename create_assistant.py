from openai import OpenAI

model = 'gpt-3.5-turbo-1106'

c = OpenAI()

assistant = c.beta.assistants.create(
    name="Aurora",
    instructions="You are a helpful, feminine assistant named Sam.",
    tools=[{"type": "retrieval"}],
    model=model,
)

print("Created new assistant:")
print(assistant.id)
