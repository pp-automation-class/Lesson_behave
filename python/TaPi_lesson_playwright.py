from playwright.sync_api import sync_playwright

browsers = ["chromium", "firefox"]

for browser_type in browsers:
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False)
        else:
            browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
        username = page.locator("//input[@name='username']")
        username.type("email", delay=1000)
        page.keyboard.press("Tab")

        password = page.locator("//input[@name='password']")
        password.type("1234", delay=1000)
        password.click()
        button = page.locator("//button")
        button.click()
        page.screenshot(path=f"{browser_type}_dev_linkmygear.png")
        browser.close()
