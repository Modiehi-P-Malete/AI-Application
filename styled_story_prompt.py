"""
Exercise: Specific and Precise Prompting
Concept: Control output style and structure using detailed instructions
Goal: Generate a story continuation in Shakespearean style with two paragraphs
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


story = "A traveler wandered into a forgotten kingdom where time seemed to stand still."

prompt = f"""
Complete the story delimited by triple backticks.

Write only two paragraphs and use the writing style of Shakespeare.

```{story}```
"""

response = get_response(prompt)

print("\nOriginal story:\n", story)
print("\nGenerated story:\n", response)