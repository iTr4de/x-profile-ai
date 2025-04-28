# app/nlp/prompt_engine.py

from typing import List

def build_prompt(username: str, tweets: List[str], topics: List[str], tone: str = "Visionary Leader") -> str:
    """
    Build a custom GPT prompt based on user's tweets, dominant topics, and selected tone.
    """
    tweets_sample = "\n".join(f"- {tweet}" for tweet in tweets[:10])  # Use first 10 tweets for brevity
    topics_text = ", ".join(topics)

    prompt = f"""
You are a world-class branding strategist.

Based on the following tweets from the Twitter user @{username}, generate:
1. A 2-sentence professional Twitter bio.
2. A 4-sentence mission statement that fits their thought leadership style, tone = '{tone}'.

Make sure to:
- Keep the writing human-like, authentic, and fluent.
- Emphasize these dominant topics: {topics_text}.
- Match the user's natural tone, which is primarily '{tone}'.
- Extract and synthesize common themes, avoiding repetition.

Recent Tweets Sample:
{tweets_sample}

Output Format:
Bio: <two sentence Twitter bio>
Mission: <four sentence mission statement>
"""

    return prompt.strip()