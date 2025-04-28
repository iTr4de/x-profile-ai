# scripts/profile_preview.py

import asyncio
import httpx

API_URL = "http://127.0.0.1:8000/api/profile/"

async def main():
    payload = {
        "username": "pierrebruynaud",  # 👈 Test with any public X (Twitter) handle
        "tone": "Visionary Leader",
        "tweet_limit": 500,
        "language": "en"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, json=payload)
        print("\n--- Profile Response ---\n")
        print(response.json())

if __name__ == "__main__":
    asyncio.run(main())