# X-Profile AI

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/fastapi-powered-brightgreen)
![License](https://img.shields.io/badge/license-proprietary-red)

**AI-powered Profile Generator from Public Twitter (X) Data**

Generates a two-line bio and mission summary from a user's top tweets, including dominant themes, tone, and engagement signals. Ideal for influencer analysis, digital legacy, and personal branding.

## ⚠️ Important: Twitter API (X) Subscription Requirement

> **Note:** Profiling real Twitter (X) users requires a paid API subscription (Basic or higher).
> 
> - Free Twitter Developer accounts **only allow posting tweets**, not reading user tweets.
> - To fetch public tweets (needed for generating profiles), you must have **Basic Tier Access** ($100/month).
> - Without a subscription, the app can still operate in **Mock Mode** using simulated tweets for testing purposes.

## Features
- Twitter API v2 integration
- BERTopic for tweet theme clustering
- ...

**AI-powered Profile Generator from Public Twitter (X) Data**

Generates a two-line bio and mission summary from a user's top tweets, including dominant themes, tone, and engagement signals. Ideal for influencer analysis, digital legacy, and personal branding.

## Features
- Twitter API v2 integration
- BERTopic for tweet theme clustering
- RoBERTa/BERT-based tone analysis
- GPT-powered profile writer
- Streamlit or React frontend (coming soon)
- Dockerized & scalable

# How to Run


## 1. Clone
```bash
git clone https://github.com/brightntech/x-profile-ai.git && cd x-profile-ai
```

## 2. Add API keys
TWITTER BEARER TOKEN + OPENAI API KEY

## 3. Run server
```bash
docker build -t x-profile-ai .
docker run -p 8000:8000 x-profile-ai
```

### 

# 🚀 X-Profile AI: Detailed Launch & Deployment Guide

## 1. Clone your repo
```bash
git clone https://github.com/your-username/x-profile-ai.git
cd x-profile-ai
```

## 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # or `venv\Scripts\activate` on Windows
```
## 3. Install dependencies
```bash
pip install -r requirements.txt
```
## 4. Download spaCy English model
```bash
python -m spacy download en_core_web_sm
```
## 5. Create .env file
```bash
touch .env
```
Add this to .env:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx  
TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAAxxxxxx
```
⚠️ Reminder: Twitter Free API can’t fetch tweets — either mock data or upgrade to billable Basic API



## 6. Required Python Libraries

Here’s your requirements.txt essentials:
```bash
fastapi
uvicorn
httpx
openai>=1.0.0
python-dotenv
pydantic
spacy
transformers
bertopic
umap-learn
hdbscan
scikit-learn
torch
```
Additional optional tools:
```bash
huggingface-hub  # if deploying on HF Spaces
```
✅ These power the NLP stack (spaCy, BERTopic, Transformers) and the FastAPI backend.

⸻

## 🔥 7. Start the API Server
```bash
uvicorn main:app --reload
```
### Access it locally:
```bash
http://127.0.0.1:8000/docs
```
###  CLI test it from another terminal:
```bash
python scripts/profile_preview.py
```

## 8. Deploying to Hugging Face Spaces (or other cloud)

If you want to deploy this as an API backend in the cloud (like on Hugging Face Spaces or Render), here are the specifics:

🛰 Hugging Face Spaces (FastAPI mode):
```bash
Create these 2 files: requirements.txt + app.py
```

This will serve as entry for Spaces (Spaces doesn’t use **main.py** by default):

### app.py (for Hugging Face Space)
```bash
from fastapi import FastAPI
from app.api.routes import router as profile_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to X-Profile AI - powered by FastAPI"}

app.include_router(profile_router, prefix="/api/profile")
```
Or symlink/rename main.py → app.py as needed.

✅ Hugging Face setup  
	•	Use “FastAPI” as your Space SDK  
	•	Set OPENAI_API_KEY and TWITTER_BEARER_TOKEN in the “Secrets” tab  
	•	Push the repo, it will auto-deploy.  


## 🧪 9. Mock Mode for Local Testing

If you don’t have Twitter Basic API:  
	•	Your backend will automatically fall back to mocked tweets  

Profile generation still works with:  
		•	Sentiment  
		•	Topic modeling  
		•	GPT-powered bio creation  

✅ Fully testable even without live Twitter access.

⸻

## 📌 Summary: Start Checklist

``` bash 
python3 -m venv venv # Create env	
venv/bin/activate # Activate source 
pip install -r requirements.txt # Install deps	
uvicorn main:app --reload # Run server in main terminal
python scripts/profile_preview.py # Test CLI in other terminal	

http://localhost:8000/docs # Check docs	
```
---

## recap

## 📂 Updating Project Structure Documentation
To keep the `structure.txt` file up-to-date with the current project layout

1. Make sure you are inside the project root:
```bash
cd /path/to/x-profile-ai/
```

2. Run this command:
```bash
tree -I '.git|__pycache__|.venv|*.pyc|*.log' > structure.txt
```
3. This will:  
	•	Generate a clean directory structure.  
	•	Ignore unnecessary folders and files (e.g., .venv, __pycache__, .git/, etc.)  
	•	Save the output into structure.txt, updating the existing file.  

If you also want to see the structure live while updating, you can use:
```bash
tree -I '.git|__pycache__|.venv|*.pyc|*.log' | tee structure.txt
```
4. After updating, commit the changes:
```bash
git add structure.txt
git commit -m "Update project structure documentation"
git push
```
📢 Note:

If the tree command is not available, install it:  
	•	macOS: brew install tree  
	•	Ubuntu: sudo apt install tree  
	•	Windows: Install Git Bash and use tree  