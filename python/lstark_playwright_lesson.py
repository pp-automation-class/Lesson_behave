from playwright.sync_api import sync_playwright

from python.playwright_lesson import context_dev

browser = ["chromium"]

for browser_type in browser:
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False)
        else:
            browser = p.firefox.launch(headless=False)
            context_dev = browser.new_context()

        context_dev.tracing.start(name="trace", screenshots=True, snapshots=True)

        page_dev = context_dev.new_page()
        page_dev.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")



