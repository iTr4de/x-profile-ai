# app/nlp/sentiment_style.py

from typing import List
from transformers import pipeline
import logging

# Load a sentiment analysis pipeline from HuggingFace
try:
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
except Exception as e:
    logging.error(f"[Sentiment Pipeline Loading Error] {e}")
    sentiment_pipeline = None

def detect_tone(tweets: List[str]) -> str:
    """
    Detect the dominant tone from a list of tweets.
    """
    if not tweets or sentiment_pipeline is None:
        return "neutral"

    try:
        results = sentiment_pipeline(tweets[:50])  # Limit to first 50 tweets for speed
        scores = {"positive": 0, "neutral": 0, "negative": 0}

        for result in results:
            label = result['label'].lower()
            if "pos" in label:
                scores["positive"] += 1
            elif "neg" in label:
                scores["negative"] += 1
            else:
                scores["neutral"] += 1

        dominant = max(scores, key=scores.get)
        return dominant

    except Exception as e:
        logging.error(f"[Tone Detection Error] {e}")
        return "neutral"