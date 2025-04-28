# scripts/test_openai_key.py

import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def test_openai_key():
    try:
        # Make a cheap minimal API call (list models)
        response = openai.models.list()
        print("✅ OpenAI API key is valid!")
    except Exception as e:
        print(f"❌ OpenAI API key failed: {e}")

if __name__ == "__main__":
    test_openai_key()