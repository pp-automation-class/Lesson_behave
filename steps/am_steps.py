from behave import step
import random
import string


def random_email():
    return "".join(random.choice(string.ascii_letters) for _ in range(7)) + "@gmail.com"


@step('am: I login as "{user_type}"')
def am_login_as_user(context, user_type):
    """
    :param context:
    :param user_type:
    """
    xpath = {
        "username": "//input[@name='username']",
        "password": "//input[@name='password']",
        "button": "//button[text()=' Login ']",
    }
    xpath_verify = "//h3[contains(text(), 'My device')]"
    users = {
        "user": {"username": "7nxjno9lr@mozmail.com", "password": "r+WLLX9qwx^:>:3"},
        "admin": {"username": "admin@cia.gov", "password": "password"},
        "guest": {"username": "guest", "password": ""},
    }
    assert user_type in users, f"Unknown user type '{user_type}'"
    context.page.fill_element(xpath["username"], users[user_type]["username"])
    context.page.fill_element(xpath["password"], users[user_type]["password"])
    context.page.click_element(xpath["button"])
    assert context.page.element_exists(
        xpath_verify, timeout=3000
    ), f"Login not successful for user type '{user_type}'"


@step('am: I fill "{text}" in element "{xpath}"')
def am_fill_text_in_element(context, text, xpath):
    if text != "Skip":
        if text == "RandomEmail":
            text = random_email()
        context.page.fill_element(xpath, text)
