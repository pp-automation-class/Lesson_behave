from colorama import Fore
from playwright.sync_api import sync_playwright


def navigate_to_page(page, url, verification_xpath):
    page.goto(url)
    page.wait_for_selector(verification_xpath, timeout=3000)


def fill_element(page, locator, value):
    if value != "Skip":
        el = page.locator(locator)
        el.fill(value)


def login(page, username, password, button="//button"):
    fill_element(page, username["locator"], username["value"])
    fill_element(page, password["locator"], password["value"])
    button_element = page.locator(button)
    button_element.click()


login_data = [
    [
        "7nxjno9lr@mozmail.com",
        "r+WLLX9qwx^:>:3",
        "//h3[contains(text(), 'My device')]",
        "Successful user login with valid credentials",
    ],
    [
        "7nxjno9lrppp@mozmail.com",
        "r+WLLX9qwx^:>:3 ",
        "//p[text()='Sorry, unrecognized username or password.']",
        "Unsuccessful user login with invalid username and valid password",
    ],
    [
        "7nxjno9lrpp@mozmail.com ",
        "xxxxx",
        " //p[text()='Sorry, unrecognized username or password.'] ",
        "Unsuccessful user login with invalid credentials",
    ],
    [
        "7nxjno9lr@mozmail.com",
        "xxxxx           ",
        " //p[text()='Sorry, unrecognized username or password.'] ",
        "Unsuccessful user login with valid username and invalid password",
    ],
    [
        "Skip",
        "xxxxx           ",
        " //div[text()='Email is required']",
        "Unsuccessful user login with empty username",
    ],
    [
        "7nxjno9lr@mozmail.com",
        "Skip",
        " //div[text()='Password is required']",
        "Unsuccessful user login with empty password",
    ],
]

for one_login in login_data:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(one_login[3])

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
            page.wait_for_selector(one_login[2].strip(), timeout=3000)

        except Exception as error:
            print(f"\t{Fore.RED}Element with XPath '{one_login[2].strip()}' does not exist: {error.name}{Fore.RESET}")
        else:
            page.wait_for_timeout(3000)

        browser.close()
