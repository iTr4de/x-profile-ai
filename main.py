# main.py

from fastapi import FastAPI
from app.api.routes import router as profile_router

app = FastAPI(
    title="X-Profile AI",
    description="AI-powered Profile Generator from Public Tweets",
    version="0.1.0",
)

# Include the profile generation API under /api/profile
app.include_router(profile_router, prefix="/api/profile")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)