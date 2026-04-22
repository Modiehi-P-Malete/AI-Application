from openai import OpenAI

client = OpenAI()

prompt = """
Write a persuasive product description for SonicPro wireless headphones.

Include the following features:
- Active Noise Cancellation (ANC)
- 40-hour battery life
- Foldable design

Target audience: music lovers and professionals
Tone: modern and engaging
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=150,
    temperature=0.7
)

print(response.choices[0].message.content)