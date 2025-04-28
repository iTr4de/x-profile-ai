# main.py

import os
import openai
import httpx
import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
from app.api.routes import router as profile_router
from app.core.validators import test_openai_key, test_twitter_bearer_token

# Load environment variables
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Auto-test OpenAI API Key
def test_openai_key_on_startup():
    try:
        openai.models.list()
        print("✅ OpenAI API key validated successfully!")
    except Exception as e:
        print(f"❌ OpenAI API key validation failed: {e}")
        raise RuntimeError("🚨 OpenAI API key is invalid. Fix your .env file.")

# Auto-test Twitter Bearer Token
async def test_twitter_bearer_token_on_startup():
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

# Initialize FastAPI app
app = FastAPI(
    title="X-Profile AI",
    description="AI-powered Profile Generator from Public Tweets",
    version="0.1.0",
)

# Health check router
health_router = APIRouter()

@health_router.get("/health", tags=["Health"])
async def health_check():
    """
    Check if OpenAI and Twitter API keys are still valid.
    """
    openai_status = "✅ OK"
    twitter_status = "✅ OK"

    # OpenAI Key Check
    try:
        openai.models.list()
    except Exception as e:
        openai_status = f"❌ {str(e)}"

    # Twitter Token Check
    try:
        headers = {
            "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"
        }
        url = "https://api.twitter.com/2/tweets/search/recent?query=twitter"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
        if response.status_code != 200:
            twitter_status = f"❌ {response.status_code} - {response.text}"
    except Exception as e:
        twitter_status = f"❌ {str(e)}"

    return {
        "openai_api": openai_status,
        "twitter_api": twitter_status,
        "status": "✅ Healthy" if openai_status.startswith("✅") and twitter_status.startswith("✅") else "❌ Issues Detected"
    }

# Startup event
@app.on_event("startup")
async def startup_event():
    test_openai_key()
    await test_twitter_bearer_token()

# Include API routes
app.include_router(profile_router, prefix="/api/profile", tags=["Profile"])
app.include_router(health_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)