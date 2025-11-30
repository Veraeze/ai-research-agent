from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://en.wikipedia.org/wiki/Artificial_intelligence")
    page.wait_for_timeout(5000)  # stays open for 5 seconds
    browser.close()