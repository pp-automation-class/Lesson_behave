LINKMYGEAR_URL = "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
VERIFY_PATH = "//h5[.='Login to Your Account']"


class LoginPage:
    def __init__(self, page):
        self.logo_img = "//img[@alt='Logo']"
        self.username_input = "//input[@name='username']"
        self.password_input = "//input[@name='password']"
        self.login_button = "//button[text()=' Login ']"
        self.header = "//h3[contains(text(), 'My device')]"
        self.page = page

    def __input_username(self, username):
        self.page.fill(self.username_input, username)

    def __input_password(self, password):
        self.page.fill(self.password_input, password)

    def __click_login(self):
        self.page.click(self.login_button)

    def navigate(self, url: str = LINKMYGEAR_URL, verify_path: str = VERIFY_PATH):
        self.page.goto(url)
        self.page.wait_for_selector(verify_path, timeout=3000)
        return self

    def login(self, username, password):
        self.__input_username(username)
        self.__input_password(password)
        self.__click_login()

    def verify_login_success(self):
        return self.page.wait_for_selector(self.header)

    def verify_login_fail(self):
        return self.page.wait_for_selector(self.logo_img)
