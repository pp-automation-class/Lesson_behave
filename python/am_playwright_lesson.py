from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
    page.wait_for_timeout(2000)
    page.wait_for_selector("//h5[.='Login to Your Account']", timeout=3000)
    username = page.locator("//input[@name='username']")
    username.fill("email")
    username.type("imall", delay=500)
    password = page.locator("//input[@name='password']")
    password.fill("1234")
    button = page.locator("//button")
    button.click()
    button.wait_for(state="visible")
    page.screenshot(path="c:\\Users\\aamal\\Pictures\\Chromium_dev_linkmygear.png")
    browser.close()
