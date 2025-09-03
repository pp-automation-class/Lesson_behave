from playwright.sync_api import sync_playwright

browser = ["chromium"]

for browser_type in browser:
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False)
        else:
            browser = p.firefox.launch(headless=False)

        page = browser.new_page()
        page.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
        username = page.locator("//input[@name='username']")
        username.fill("lauravstesting53@gmail.com")
        password = page.locator("//input[@name='password']")
        password.fill("T8st8ng38!1")
        button = page.locator("//button")
        button.click()
        button.wait_for(state="visible")
        browser.close()
