# Intelligent Research & Web-Scraping Agent

This AI agent is designed to search the internet, scrape real-time information from multiple websites, and summarize the content using AI models.

Tools used:
-playwright: opens real websites like a browser
-beautifulsoup4: cleans and extracts text from HTML
-requests: handles basic HTTP requests
-transformers: HuggingFace models (your summarizer)
-torch: backend for running the AI model
-langchain: agent structure / orchestration
-python-dotenv: manage environment variables (future-safe)
-streamlit: for optional UI/dashboard later
-pandas: for future data processing or reports

## Key Features
- Autonomous web scraping
- Multi-source information gathering
- AI-powered summarization
- Clean architecture using agent design
- Real-world industry tools

## Agent Architecture

The system works in this order:

1. The user provides a topic in main.py
2. The agent decides where and how to search
3. The scraper extracts information from live websites
4. The summarizer condenses the information
5. A clean report is saved in /output