"""
Exercise: Creating a Reusable Prompt Function
Concept: Encapsulating API requests inside a helper function
Goal: Simplify prompt experimentation by reusing the same API call logic
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


response = get_response("What is prompt engineering?")
print(response)