from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
    username = page.locator("//input[@name='username']")
    username.fill("katedtest@gmail.com")
    password = page.locator("//input[@name='password']")
    password.fill("1234567890")
    button = page.locator("//button")
    button.click()
    logout_button = "//span[text()='Log out']"
    assert logout_button
