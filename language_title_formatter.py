"""
Exercise: Custom Output Formatting
Concept: Control the structure of model responses using explicit output templates
Goal: Detect language of a text and generate a suitable title in a structured format
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


text = """
Artificial intelligence is transforming industries across the world.
Companies are using machine learning to improve efficiency and innovation.
"""


# Create instructions
instructions = (
    "Determine the language of the following text and generate a suitable title for it. "
    "Use the provided output format. The text will be delimited using triple backticks."
)

# Define output format
output_format = (
    "Text:\n"
    "Language:\n"
    "Title:"
)

# Create final prompt
prompt = f"""
{instructions}

Output format:
{output_format}

Text to analyze:
```{text}```
"""

response = get_response(prompt)

print(response)