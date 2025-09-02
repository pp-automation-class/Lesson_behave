from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


class LstarkLoginPage:
    def __init__(self, driver):
        self.logo_img = "//img[@alt='Logo']"
        self.username_input = "//input[@name='email']"
        self.password_input = "//input[@name='password']"
        self.login_button = "//button[text()=' Login ']"
        self.header = "//h5"

    def input_username(self, username):
        page.fill(self.username_input, username)

    def input_password(self, password):
        page.fill(self.password_input, password)

    def click_login_button(self):
        page.click(self.login_button)

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

    def verify_login_success(self):
        page.wait_for_selector(self.header)

    def verify_login_fail(self):
        page.wait_for_selector(self.logo_img)
