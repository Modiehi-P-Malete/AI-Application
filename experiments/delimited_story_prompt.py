"""
Exercise: Delimited Prompts with f-Strings
Concept: Use delimiters to clearly separate input text from instructions
Goal: Generate a continuation of a story using triple backticks
"""

from openai import OpenAI

client = OpenAI()

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


story = "A young explorer discovered a mysterious door hidden inside an ancient tree."

# Create prompt using delimiters
prompt = f"""
Complete the story delimited by triple backticks.

```{story}```
"""

response = get_response(prompt)

print("\nOriginal story:\n", story)
print("\nGenerated story:\n", response)