"""
Exercise: Prompt Engineering Refinement
Concept: Improving prompts by specifying tone, audience, and output style
Goal: Generate a poem about ChatGPT written in simple English for children
"""

from openai import OpenAI

client = OpenAI()

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content


# Craft a prompt that follows the instructions
prompt = "Write a short poem about ChatGPT using basic English that a child can understand."

# Get the response
response = get_response(prompt)

print(response)