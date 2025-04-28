# X-Profile AI

**AI-powered Profile Generator from Public Twitter (X) Data**

Generates a two-line bio and mission summary from a user's top tweets, including dominant themes, tone, and engagement signals. Ideal for influencer analysis, digital legacy, and personal branding.

## Features
- Twitter API v2 integration
- BERTopic for tweet theme clustering
- RoBERTa/BERT-based tone analysis
- GPT-powered profile writer
- Streamlit or React frontend (coming soon)
- Dockerized & scalable

## How to Run

```bash
# 1. Clone
git clone https://github.com/brightntech/x-profile-ai.git && cd x-profile-ai

# 2. Add API keys
cp .env.example .env

# 3. Run server
docker build -t x-profile-ai .
docker run -p 8000:8000 x-profile-ai