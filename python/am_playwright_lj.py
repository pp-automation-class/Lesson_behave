from playwright.sync_api import sync_playwright, Browser


class Livejournal:
    def __init__(self, browser: Browser):
        self.browser = browser

    def register(self):
        context = self.browser.new_context()
        page = context.new_page()
        page.goto("https://www.livejournal.com/create/")
        page.wait_for_selector("//h2[.='Creating a New Journal']", timeout=3000)

        username = "Stepan2522089"
        email = "colonelcasad+lj001@gmail.com"
        password = "n+D20964//Auu"
        birthday = ("January", "1", "1959")

        page.locator("//input[@name='username']").fill(username)
        page.locator("//input[@name='email']").fill(email)
        page.locator("//input[@id='password']").fill(password)
        page.locator("//select[@id='day']").select_option(birthday[1])
        page.locator("//select[@id='month']").select_option(birthday[0])
        page.locator("//select[@id='year']").select_option(birthday[2])
        page.keyboard.press('Tab')
        page.locator("//button[@title='Create account']").click()

        page.wait_for_timeout(5000)

    # end register


with sync_playwright() as p:
    browser: Browser = p.chromium.launch(headless=False)

    x = Livejournal(browser)

    x.register()

    browser.close()
