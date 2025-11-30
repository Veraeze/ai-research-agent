# agent.py
# This is the brain of the system

# 1. Receive topic from main.py
# 2. Select correct websites
# 3. Send websites to scraper
# 4. Send scraped data to summarizer
# 5. Save final output

from scraper import run_scraper
from summarizer import summarize_all

def run_agent():
    """
    Main function to run the AI Research Agent.
    1. Scrape live websites
    2. Summarize scraped data
    3. Save summaries to /output
    """
    print(" Starting AI Research Agent...")

    # Step 1: Scrape websites
    run_scraper()  # calls scraper.py to collect and save raw text
    print(" Scraping complete. Raw data saved in /data.")

    # Step 2: Summarize scraped data
    summarize_all()  # calls summarizer.py to process all files
    print(" Summarization complete. Summaries saved in /output.")

if __name__ == "__main__":
    run_agent()