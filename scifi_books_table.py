"""
Exercise: Generating Structured Outputs (Tables)
Concept: Instruct the model to produce structured output
Goal: Generate a table of science fiction books with specific columns
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


# Create the prompt
prompt = (
    "Generate a table containing 10 books I should read if I am a science fiction lover. "
    "The table must contain the columns: Title, Author, and Year."
)

response = get_response(prompt)

print(response)