# app/core/validators.py

import os
import openai
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup keys
openai.api_key = os.getenv("OPENAI_API_KEY")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

def test_openai_key():
    """
    Test if the OpenAI API key is valid.
    """
    try:
        openai.models.list()
        print("✅ OpenAI API key validated successfully!")
    except Exception as e:
        print(f"❌ OpenAI API key validation failed: {e}")
        raise RuntimeError("🚨 OpenAI API key is invalid. Fix your .env file.")

async def test_twitter_bearer_token():
    """
    Test if the Twitter API Bearer Token is valid by making a public API request.
    """
    if not TWITTER_BEARER_TOKEN:
        print("❌ No Twitter Bearer Token found in .env file.")
        raise RuntimeError("🚨 Twitter Bearer Token missing!")

    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"
    }
    url = "https://api.twitter.com/2/tweets/search/recent?query=twitter"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 200:
        print("✅ Twitter Bearer Token validated successfully!")
    elif response.status_code == 401:
        print("❌ Invalid Twitter Bearer Token: Unauthorized access.")
        raise RuntimeError("🚨 Invalid Twitter Bearer Token!")
    elif response.status_code == 403:
        print("❌ Forbidden: Token might not have access (Basic API Plan may be required).")
        raise RuntimeError("🚨 Twitter Bearer Token forbidden - insufficient access level.")
    elif response.status_code == 429:
        print("⚠️  Twitter API rate limit exceeded (429 Too Many Requests). Skipping Twitter check at startup.")
    else:
        print(f"❌ Unexpected Twitter API response: {response.status_code} - {response.text}")
        raise RuntimeError(f"🚨 Twitter API unexpected error: {response.status_code}")