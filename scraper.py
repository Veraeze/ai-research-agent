# scraper.py
# 1. Open a website using Playwright
# 2. Wait for content to fully load
# 3. Extract main text using BeautifulSoup
# 4. Clean the text
# 5. Save raw text into /data folder

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os


def scrape_website(url, filename):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000, wait_until="domcontentloaded")
        page.wait_for_timeout(5000)

        content = page.content()
        browser.close()

    soup = BeautifulSoup(content, "html.parser")

    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text(separator="\n")
    cleaned_text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])

    os.makedirs("data", exist_ok=True)

    with open(f"data/{filename}.txt", "w", encoding="utf-8") as file:
        file.write(cleaned_text)

    print(f" Saved: data/{filename}.txt")


def run_scraper():
    websites = {
        "wikipedia": "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "ibm": "https://www.ibm.com/topics/artificial-intelligence",
        "nature": "https://www.nature.com/subjects/artificial-intelligence"
    }

    for name, url in websites.items():
        scrape_website(url, name)