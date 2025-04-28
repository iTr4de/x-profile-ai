# app/api/routes.py

from fastapi import APIRouter, HTTPException
from app.generator.profile_writer import generate_profile
from app.models.user_profile import ProfileRequest, ProfileResponse

router = APIRouter()

@router.post("/", response_model=ProfileResponse, summary="Generate Twitter Profile Summary")
async def create_profile(data: ProfileRequest):
    """
    Generate a profile bio + mission statement from a Twitter user's public tweets.
    """
    try:
        return await generate_profile(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))