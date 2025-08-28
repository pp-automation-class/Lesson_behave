from playwright.sync_api import sync_playwright


browsers = ["chromium"]

for browser_type in browsers:
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False)
        else:
            browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
        username = page.locator("//input[@name='username']")
        username.click()
        username.fill("akr.autotest@gmail.com")
        password = page.locator("//input[@name='password']")
        password.click()
        password.type("12345", delay=500)
        button = page.locator("//button")
        button.click()
        # page.screenshot(path=F"{browser_type}_dev_linkmygear.png")
        browser.close()
