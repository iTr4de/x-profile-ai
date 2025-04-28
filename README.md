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

## How to Run

```bash
# 1. Clone
git clone https://github.com/brightntech/x-profile-ai.git && cd x-profile-ai

# 2. Add API keys
cp .env.example .env

# 3. Run server
docker build -t x-profile-ai .
docker run -p 8000:8000 x-profile-ai

Perfect!
Here’s a professional README update you can copy into your README.md —
it adds a clean “How to Update Project Structure” section for your structure.txt!

⸻

📄 Suggested Addition to README.md

## 📂 Updating Project Structure Documentation

To keep the `structure.txt` file up-to-date with the current project layout:

### 1. Make sure you are inside the project root:

```bash
cd /path/to/x-profile-ai/

2. Run this command:

tree -I '.git|__pycache__|.venv|*.pyc|*.log' > structure.txt

✅ This will:
	•	Generate a clean directory structure.
	•	Ignore unnecessary folders and files (e.g., .venv, __pycache__, .git/, etc.)
	•	Save the output into structure.txt, updating the existing file.

If you also want to see the structure live while updating, you can use:

tree -I '.git|__pycache__|.venv|*.pyc|*.log' | tee structure.txt

3. After updating, commit the changes:

git add structure.txt
git commit -m "Update project structure documentation"
git push

📢 Note:

If the tree command is not available, install it:
	•	macOS: brew install tree
	•	Ubuntu: sudo apt install tree
	•	Windows: Install Git Bash and use tree

⸻

✅ Keeping structure.txt updated ensures the repo stays clean, transparent, and developer-friendly.