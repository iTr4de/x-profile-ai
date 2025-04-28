# app/nlp/topic_modeling.py

from typing import List
from bertopic import BERTopic

def extract_topics(tweets: List[str], top_n: int = 5) -> List[str]:
    """
    Extract dominant topics from a list of tweets using BERTopic.
    """
    if not tweets:
        return []

    try:
        model = BERTopic(verbose=False)
        topics, _ = model.fit_transform(tweets)

        topic_info = model.get_topic_info()
        top_topics = topic_info.head(top_n + 1)[1:]  # Skip the outlier class (-1)

        extracted_topics = []
        for _, row in top_topics.iterrows():
            topic_name = row["Name"]
            # Simplify: remove "Topic #" prefix if it exists
            if topic_name.lower().startswith("topic"):
                topic_name = topic_name.split(":", 1)[-1].strip()
            extracted_topics.append(topic_name)

        return extracted_topics

    except Exception as e:
        print(f"[Topic Modeling Error] {e}")
        return []