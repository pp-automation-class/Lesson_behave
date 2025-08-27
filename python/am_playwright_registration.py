import random
import string

from colorama import Fore
from playwright.sync_api import sync_playwright


def random_email():
    return "".join(random.choice(string.ascii_letters) for _ in range(7)) + "@gmail.com"


def navigate_to_page(page, url, verification_xpath):
    page.goto(url)
    page.wait_for_selector(verification_xpath, timeout=3000)


def fill_element(page, locator, value):
    if value != "Skip":
        if value == "RandomEmail":
            value = random_email()
        page.locator(locator).fill(value)

def click_element(page, locator):
    if locator != "Skip":
        page.locator(locator).click()

registration_data = [
    [
        "RandomEmail",
        "//h3[contains(text(), 'My device')]",
        "//button[text()=' Register ']",
        "Successful user registration with valid email",
    ],
    [
        "7nxjno9lr@mozmail.com",
        "//p[contains(text(), 'The user already exists')]",
        "//button[text()=' Register ']",
        "Unsuccessful user registration with existing email",
    ],
    [
        "Skip",
        "//div[text()='Please enter you email address']",
        "Skip",
        "Unsuccessful user registration with empty email",
    ],
    [
        "xxxxx",
        "//div[text()='Please enter a valid email address']",
        "Skip",
        "Unsuccessful user registration with invalid email",
    ],
]

for one_reg in registration_data:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(one_reg[3])

        navigate_to_page(
            page,
            "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
            "//h5[.='Login to Your Account']",
        )

        page.locator("//a[@href='#/register']").click()
        page.wait_for_selector("//h5[text()='Create an Account']", timeout=3000)

        page.locator("//input[@class='el-input__inner']").click()
        fill_element(page, "//input[@class='el-input__inner']", one_reg[0])
        click_element(page, "//span[@class='el-checkbox__inner']")
        click_element(page, one_reg[2])

        try:
            page.wait_for_selector(one_reg[1], timeout=3000)

        except Exception as error:
            print(f"\t{Fore.RED}Element with XPath '{one_reg[1]}' does not exist: {error.name}{Fore.RESET}")
        else:
            page.wait_for_timeout(3000)

        browser.close()
