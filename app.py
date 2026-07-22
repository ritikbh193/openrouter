from openai import OpenAI
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()


api_key = os.getenv('router')

# cohere/north-mini-code:free

# "google/gemma-3-12b-it"


client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

response = client.chat.completions.create(
    model="google/gemma-3-12b-it",   # Change to any Gemma model
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": "what is python in short"
        }
    ],
    temperature=0.7,
    max_tokens=500,
)

print(response.choices[0].message.content)