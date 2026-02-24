
from openai import OpenAI # Create a client (make sure your OPENAI_API_KEY is set in your environment (.env file ))
client = OpenAI()# Replace the prompt below with your own question or instruction

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,
  
    # Enter your prompt
    messages=[{"role": "user", "content": "Can you tell me about MERN stack job market"}]
)

print(response.choices[0].message.content)
response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
        {
"role":"system",
"content":"You are a programming teacher. Explain concepts simply with examples."
        },
        {
"role":"user",
"content":"Explain JavaScript closures"
        }
    ]
)

print(response.choices[0].message.content)