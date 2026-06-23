"""
Exercise: Creating a Reusable Prompt Function
Concept: Encapsulating API requests inside a helper function
Goal: Simplify prompt experimentation by reusing the same API call logic
"""

import os
try:
    from openai import OpenAI
except ImportError as exc:
    raise ImportError(
        "The openai package is required. Install it with 'pip install openai'."
    ) from exc

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content


response = get_response("What is prompt engineering?")
print(response)