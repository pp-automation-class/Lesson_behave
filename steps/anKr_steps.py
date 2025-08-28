"""
Step definitions for web interactions using the Lingh framework.
"""

from behave import step
from pages.login import LoginPage


@step('anKr I login as "{user_type}"')
def ankr_login_as_user(context, user_type):
    """
    Args:
        user_type: Type of user to login as
        context (behave.runner.Context):
    """

    user_credentials = {
        "user": {"username": "akr.autotest@gmail.com", "password": "12345"},
        "admin": {"username": "akr.autotest@gmail.com", "password": "13579"}
    }

    # fill username

    def fill_text_in_element(context, text, xpath):
        if text != 'Skip':
            context.page.fill_element(xpath, text)

    user_name_xpath = LoginPage().username
    # fill_text_in_element(context, user_name, user_name_xpath)
    fill_text_in_element(context, user_credentials[user_type][0], user_name_xpath)

    # fill password
    password_xpath = LoginPage().password
    # fill_text_in_element(context, password, password_xpath)
    fill_text_in_element(context, user_credentials[user_type][1], password_xpath)

    # Click login button
    def click_on_element(context, xpath):
        context.page.click_element(xpath)

    login_button_xpath = LoginPage().login_button
    click_on_element(context, login_button_xpath)


@step('anKr I verify element page title contains text "Account"')
def ankr_verify_element_contains_text_with_pom(context, expected_text):
    login_page = LoginPage()
    actual_text = context.page.get_element_text(login_page.header)
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in '{actual_text}'"
