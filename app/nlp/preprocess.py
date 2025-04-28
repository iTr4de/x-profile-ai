# app/nlp/preprocess.py

import re
import string
from typing import List

import spacy

# Load English tokenizer and tagger from spaCy
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

URL_PATTERN = re.compile(r"https?://\S+|www\.\S+")
MENTION_PATTERN = re.compile(r"@\w+")
HASHTAG_PATTERN = re.compile(r"#\w+")
EMOJI_PATTERN = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)

def clean_text(text: str) -> str:
    """
    Clean a single tweet's text: remove URLs, mentions, hashtags, emojis, punctuation, etc.
    """
    text = text.lower()
    text = URL_PATTERN.sub("", text)
    text = MENTION_PATTERN.sub("", text)
    text = HASHTAG_PATTERN.sub("", text)
    text = EMOJI_PATTERN.sub("", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_tweets(tweets: List[str]) -> List[str]:
    """
    Preprocess a list of tweets.
    """
    cleaned_tweets = [clean_text(tweet) for tweet in tweets]

    # Optional: remove very short tweets
    cleaned_tweets = [tweet for tweet in cleaned_tweets if len(tweet.split()) > 3]

    return cleaned_tweets