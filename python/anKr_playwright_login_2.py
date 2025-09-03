from playwright.sync_api import sync_playwright


def navigate_to_page(page, url, verification_xpath):
    page.goto(url)
    page.wait_for_selector(verification_xpath, timeout=5000)


def fill_element(page, locator, value):
    if value != "Skip":
        page.locator(locator).fill(value)


def login(page, username, password, button="//button"):
    fill_element(page, username["locator"], username["value"])
    fill_element(page, password["locator"], password["value"])
    page.locator(button).click()


VALID_USERNAME = "akr.autotest@gmail.com"


login_data = [
    [
        VALID_USERNAME,
        "12345",
        "//h3[contains(text(), 'My device')]",
        "Successful user login with valid credentials",
    ],
    [
        "autotest@gmail.com",
        "13579 ",
        "//p[text()='Sorry, unrecognized username or password.']",
        "Unsuccessful user login with invalid username and valid password",
    ],
    [
        VALID_USERNAME,
        "13579",
        " //p[text()='Sorry, unrecognized username or password.'] ",
        "Unsuccessful user login with invalid credentials",
    ],
    [
        "autotest@gmail.com",
        "12345",
        " //p[text()='Sorry, unrecognized username or password.'] ",
        "Unsuccessful user login with valid username and invalid password",
    ],
    [
        "Skip",
        "12345",
        " //div[text()='Email is required']",
        "Unsuccessful user login with empty username",
    ],
    [
        VALID_USERNAME,
        "Skip",
        " //div[text()='Password is required']",
        "Unsuccessful user login with empty password",
    ],
    [
        VALID_USERNAME,
        "12345      ",
        " //div[text()='Password is required']",
        "Unsuccessful user login with with trailing space",
    ],
]

for one_login in login_data:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        test_name = one_login[3]
        expected_xpath = one_login[2].strip()

        print(f"Test: {test_name}")

        navigate_to_page(
            page,
            "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
            "//h5[.='Login to Your Account']",
        )

        login(
            page,
            {"locator": "//input[@name='username']", "value": one_login[0].strip()},
            {"locator": "//input[@name='password']", "value": one_login[1].strip()},
        )

        try:
            page.wait_for_selector(expected_xpath, timeout=5000)
        except Exception as error:
            print(f"\tResult: FAIL (Expected element '{expected_xpath}' not found: {error})")
        else:
            print(f"\tResult: PASS (Expected element '{expected_xpath}' found)")

        browser.close()
