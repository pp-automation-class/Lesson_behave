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





# Playwright lesson
#
#
# browsers = ["chromium"]
#
# for browser_type in browsers:
#     with sync_playwright() as p:
#         if browser_type == "chromium":
#             browser = p.chromium.launch(headless=False)
#         else:
#             browser = p.firefox.launch(headless=False)
#         context_dev = browser.new_context()
#
#         context_dev.tracing.start(name="trace", screenshots=True, snapshots=True)
#
#         page_dev = context_dev.new_page()
#         page_dev.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
#
#         # context_app = browser.new_context()
#         # page_app = context_app.new_page()
#         # page_app.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
#
#         # page_dev.get_by_label("Sign in")
#         # page_dev.get_by_text("Sign in")
#         # page_dev.get_by_alt_text("Logo")
#         #
#         # page_dev.locator("div.dialog-off-canvas-main-canvas")
#         #
#         # page_dev.locator("//div[@class='dialog-off-canvas-main-canvas']")
#
#         # page.wait_for_selector("//button1", timeout=3000)
#         # page.wait_for_timeout(2000)
#         username = page_dev.locator("//input[@name='username']")
#         username.fill("email")
#         # username.type("email", delay=500)
#         # username.click()
#         password = page_dev.locator("//input[@name='password']")
#         password.fill("1234")
#         page_dev.keyboard.press("Enter")
#         # password.click()
#         # button = page.locator("//button")
#         # button.click()
#         # button.wait_for(state="visible")
#         page_dev.screenshot(path=f"{browser_type}_dev_linkmygear.png")
#
#         context_dev.tracing.stop(path="../trace.zip")
#         browser.close()
