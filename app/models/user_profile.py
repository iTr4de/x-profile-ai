# app/models/user_profile.py

from pydantic import BaseModel
from typing import Optional

class ProfileRequest(BaseModel):
    username: str
    tone: Optional[str] = "Visionary Leader"
    tweet_limit: Optional[int] = 300
    language: Optional[str] = "en"

class ProfileResponse(BaseModel):
    bio: str
    mission: str