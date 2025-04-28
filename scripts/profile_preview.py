# scripts/profile_preview.py

import asyncio
import httpx

API_URL = "http://127.0.0.1:8000/api/profile/"

async def main():
    payload = {
        "username": "pierrebruynaud",  # Or another public Twitter user
        "tone": "Visionary Leader",
        "tweet_limit": 10,        # << Reduced to 10 to avoid 429 errors
        "language": "en"
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(API_URL, json=payload)
        print("\n--- Profile Response ---\n")
        print(response.json())

if __name__ == "__main__":
    asyncio.run(main())