# 🤖 AI Browser Scraper with Python & GPT-4o

This repo shows how to build an AI-powered web scraper using [Browser Use](https://docs.browser-use.com/) — a Python framework that lets a large language model (LLM) control your real browser.

It scrapes dynamic websites like Twitter (X), including pages that rely on JavaScript or require login sessions, and returns structured data with minimal code.

## 🚀 What This Project Does

-   Launches your actual Chrome browser (with your cookies & sessions)
-   Uses GPT-4o to navigate the web and extract content
-   Returns structured output using Pydantic models
-   Scrapes Apify’s latest tweets as a working example

---

## 🧱 Tech Stack

-   Python 3.8+
-   [Browser Use](https://docs.browser-use.com/)
-   [Playwright](https://playwright.dev/)
-   OpenAI GPT-4o (requires an API key)
-   Pydantic (for typed outputs)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ai-browser-scraper.git
cd ai-browser-scraper
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install


⸻

🔐 Setup
	1.	Create a .env file:

touch .env.example .env


	2.	Paste your OpenAI API key inside .env:

OPENAI_API_KEY=sk-...


	3.	(Optional) Update your Chrome path inside main.py if you’re not on MacOS.

⸻

▶️ Run It

python main.py

You’ll see:
	•	A Chrome browser window open on Apify’s X page
	•	GPT-4o navigating and extracting data from the 3 most recent posts
	•	Clean output saved to a JSON file:

⸻

🛠 Customize It
	•	Want to scrape Instagram, Amazon, or Reddit instead? Just change the initial_actions URL and update the prompt.
	•	Want to run it for multiple profiles? Wrap the task in a loop and switch URLs dynamically.
	•	Want to extract more data (likes, timestamps)? Update the Pydantic model and your task prompt accordingly.

⸻

📎 Requirements
	•	Python 3.8+
	•	Access to an LLM API key (the example is using OpenAI GPT-4o)
	•	Google Chrome installed
```
