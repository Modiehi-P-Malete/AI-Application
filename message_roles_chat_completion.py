
from openai import OpenAI

client = OpenAI()

# The conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": "I am preparing event for my friend marriage"}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=conversation_messages
)

print(response.choices[0].message.content)