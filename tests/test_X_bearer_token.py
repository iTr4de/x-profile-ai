# scripts/test_X_bearer_token.py

import os
import asyncio
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read Twitter Bearer Token
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

async def test_twitter_bearer_token():
    """
    Test if the Twitter API Bearer Token is valid by making a public API request.
    """
    if not TWITTER_BEARER_TOKEN:
        print("❌ No Twitter Bearer Token found in .env file.")
        return

    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"
    }
    url = "https://api.twitter.com/2/tweets/search/recent?query=twitter"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 200:
        print("✅ Twitter Bearer Token is valid!")
    elif response.status_code == 401:
        print("❌ Invalid Twitter Bearer Token: Unauthorized access.")
    elif response.status_code == 403:
        print("❌ Forbidden: This token might not have the right access level (Basic plan needed).")
    else:
        print(f"❌ Unexpected response: {response.status_code} - {response.text}")

if __name__ == "__main__":
    asyncio.run(test_twitter_bearer_token())