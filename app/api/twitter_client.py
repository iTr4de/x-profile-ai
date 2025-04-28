# app/api/twitter_client.py

import os
import httpx
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_API_URL = "https://api.twitter.com/2"

headers = {
    "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}",
}

async def fetch_user_id(username: str) -> str:
    """
    Fetch the Twitter User ID based on username.
    """
    url = f"{TWITTER_API_URL}/users/by/username/{username}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()["data"]["id"]

async def fetch_user_tweets(username: str, max_results: int = 300) -> List[str]:
    """
    Fetch recent tweets from a user's timeline.
    """
    user_id = await fetch_user_id(username)
    url = f"{TWITTER_API_URL}/users/{user_id}/tweets"
    params = {
        "max_results": min(max_results, 100),  # Twitter API limits to 100 per call
        "tweet.fields": "text,created_at,public_metrics",
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        tweets = response.json().get("data", [])
        return [tweet["text"] for tweet in tweets]