from playwright.sync_api import sync_playwright

# browsers = ["chromium", "firefox"]
browsers = ["chromium"]

for browser_type in browsers:
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False)
        else:
            browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
        # page.wait_for_selector("//button1", timeout=3000)
        # page.wait_for_timeout(2000)
        username = page.locator("//input[@name='username']")
        username.fill("email")
        # username.type("email", delay=500)
        # username.click()
        password = page.locator("//input[@name='password']")
        password.fill("1234")
        page.keyboard.press("Enter")
        # password.click()
        # button = page.locator("//button")
        # button.click()
        # button.wait_for(state="visible")
        page.screenshot(path=f"{browser_type}_dev_linkmygear.png")
        browser.close()
