# app/generator/profile_writer.py

import os
import openai
import logging

from app.api.twitter_client import fetch_user_tweets
from app.nlp.preprocess import preprocess_tweets
from app.nlp.topic_modeling import extract_topics
from app.nlp.sentiment_style import detect_tone
from app.nlp.prompt_engine import build_prompt
from app.models.user_profile import ProfileRequest, ProfileResponse

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_profile(data: ProfileRequest) -> ProfileResponse:
    """
    Full pipeline: Fetch tweets → Preprocess → Extract topics → Detect tone → Build prompt → Query GPT → Return Profile
    """
    try:
        # Step 1: Fetch user's tweets
        tweets = await fetch_user_tweets(data.username, data.tweet_limit)

        if not tweets:
            raise ValueError("No tweets found for this user.")

        # Step 2: Preprocess tweets
        cleaned_tweets = preprocess_tweets(tweets)

        # Step 3: Extract topics
        topics = extract_topics(cleaned_tweets)

        # Step 4: Detect tone
        dominant_tone = detect_tone(cleaned_tweets)

        # Step 5: Build prompt for GPT
        prompt = build_prompt(
            username=data.username,
            tweets=cleaned_tweets,
            topics=topics,
            tone=data.tone or dominant_tone,
        )

        # Step 6: Query GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can downgrade to "gpt-3.5-turbo" for cost savings
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=600,
        )

        generated_text = response["choices"][0]["message"]["content"]

        # Step 7: Parse GPT Output
        bio, mission = parse_gpt_output(generated_text)

        return ProfileResponse(bio=bio, mission=mission)

    except Exception as e:
        logging.error(f"[Profile Generation Error] {e}")
        raise e

def parse_gpt_output(generated_text: str) -> (str, str):
    """
    Parses the GPT output into bio and mission components.
    """
    bio = ""
    mission = ""

    try:
        lines = generated_text.splitlines()
        for line in lines:
            if line.lower().startswith("bio:"):
                bio = line.split(":", 1)[1].strip()
            elif line.lower().startswith("mission:"):
                mission = line.split(":", 1)[1].strip()
        
        if not bio or not mission:
            raise ValueError("Could not parse GPT output properly.")

    except Exception as e:
        logging.error(f"[GPT Output Parsing Error] {e}")
        raise e

    return bio, mission