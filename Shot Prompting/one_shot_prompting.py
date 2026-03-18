# one_shot_prompting.py
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize client
client = OpenAI()

prompt_one_shot = """Classify sentiment as 1-5 (negative to positive):
1. Love these! = 5
2. Unbelievably good! = 
3. Shoes fell apart on the second use. = 
4. The shoes look nice, but they aren't very comfortable. = 
5. Can't wait to show them off! =
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt_one_shot}],
    max_tokens=100
)

print("One-Shot Result:\n", response.choices[0].message.content)