from playwright.sync_api import sync_playwright, Browser


class Xwitter:
    def __init__(self, browser: Browser):
        self.browser = browser

    def register(self):
        context = self.browser.new_context()
        page = context.new_page()
        page.goto("https://x.com")
        page.locator("//a[.//span[.='Create account']]").click()
        page.wait_for_selector("//h1[.//span[.='Create your account']]", timeout=3000)

        username = "OneUser"
        email = "colonelcasad+x001@gmail.com"
        birthday = ("January", "1", "1909")

        page.locator("//input[@name='name']").fill(username)
        if page.locator("//input[@name='phone_number']"):
            page.locator("//button[.//span[.='Use email instead']]").click()
        page.locator("//input[@name='email']").fill(email)

        page.locator(
            "//label[.//span[.='Month']]/following-sibling::select"
        ).select_option(birthday[0])
        page.locator(
            "//label[.//span[.='Day']]/following-sibling::select"
        ).select_option(birthday[1])
        page.locator(
            "//label[.//span[.='Year']]/following-sibling::select"
        ).select_option(birthday[2])

        button = page.locator("(//button[.//span[.='Next']])[1]")
        page.wait_for_timeout(2000)  # Important! Must be paused
        button.hover()

        # page.wait_for_selector("//button[contains(@class,'r-oelmt8')][.//span[.='Next']]", timeout=5000)

        page.locator("//button[contains(@class,'r-oelmt8')][.//span[.='Next']]").click()

        page.wait_for_timeout(5000)

    # end register


with sync_playwright() as p:
    browser: Browser = p.chromium.launch(headless=False)

    x = Xwitter(browser)

    x.register()

    browser.close()
