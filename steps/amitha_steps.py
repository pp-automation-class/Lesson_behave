from behave import step

from steps.steps import fill_text_in_element, click_on_element
from pages.login import LoginPage


@step('Login as "{login_name}"')
def am_login(context, login_name):
    user_credentials = {
        "user": ("amitha04@gmail.com", "Mypassword"),
        "admin": ("pcs.automationclass@gmail.com", "xxxxxx")
    }
    user_name_xpath = LoginPage().username
    fill_text_in_element(context, user_credentials[login_name][0], user_name_xpath)

    password_xpath = LoginPage().password
    fill_text_in_element(context, user_credentials[login_name][1], password_xpath)

    login_button_xpath = LoginPage().login_button
    click_on_element(context, login_button_xpath)
