"""
Exercise: Writing Specific Prompts
Concept: Provide clear instructions including audience and length
Goal: Explain JavaScript to beginners in no more than 5 sentences
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

prompt = "Explain JavaScript to a beginner in no more than five sentences."

response = get_response(prompt)

print(response)