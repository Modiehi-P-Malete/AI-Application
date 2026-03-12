"""
Exercise: Conditional Prompting
Concept: Introduce logic into prompts similar to if-else statements
Goal: Generate a title only if the text contains more than one sentence
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
Artificial intelligence is rapidly advancing. Many industries are adopting AI tools to improve productivity.
"""


# Instructions with conditional logic
instructions = (
    "Determine the language of the given text and count the number of sentences it contains. "
    "If the text has more than one sentence, generate a suitable title for it. "
    "If the text has only one sentence, write 'N/A' for the title. "
    "The text will be provided inside triple backticks.\n\n"
)

# Define output structure
output_format = (
    "Output format:\n"
    "Text:\n"
    "Language:\n"
    "Number of sentences:\n"
    "Title:\n\n"
)

# Build prompt
prompt = instructions + output_format + f"```{text}```"

response = get_response(prompt)

print(response)