from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


class DevicesPage:
    def __init__(self, driver):
        self.logo_img = "//img[@alt='Logo']"
        self.device_list = "//input[@name='email']"
        self.news_button = "//input[@name='password']"
        self.settings_button = "//button[text()=' Login ']"
        self.header = "//h5"

    def go_to_news(self):
        page.click(self.news_button)

    def go_to_settings(self):
        page.click(self.settings_button)

    def verify_on_devices_page(self):
        page.wait_for_selector(self.header)

    def verify_on_news_page(self):
        page.wait_for_selector(self.logo_img)
