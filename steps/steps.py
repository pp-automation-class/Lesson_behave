"""
Step definitions for web interactions using the Lingh framework.
"""

from behave import step
from pages.login import LoginPage


@step('I navigate to "{url}"')
def navigate_to_url(context, url):
    if url == 'https://dev.linkmygear.com':
        url = 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com'
    context.page.navigate(url)


@step('I navigate to "{env}" environment')
def navigate_to_env(context, env):
    environments = {
        'dev': 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com',
        'prod': 'https://app.linkmygear.com'
    }
    context.page.navigate(environments[env])


@step('I click on "{xpath}"')
def click_on_element(context, xpath):
    """
    Click on an element identified by XPath.

    :param context: Behave context
    :param xpath: XPath selector for the element
    """
    context.page.click_element(xpath)


@step('I fill "{text}" in element "{xpath}"')
def fill_text_in_element(context, text, xpath):
    """
    Fill text in an element identified by XPath.

    Args:
        context: Behave context
        text: Text to fill in the element
        xpath: XPath selector for the element
    """
    if text != 'Skip':
        context.page.fill_element(xpath, text)


@step('I verify element "{xpath}" exists')
def verify_element_exists(context, xpath):
    """
    Verify that an element identified by XPath exists.

    Args:
        context: Behave context
        xpath: XPath selector for the element
    """
    context.page.verify_element_exists(xpath)


@step('I verify element "{xpath}" contains text "{expected_text}"')
def verify_element_contains_text(context, xpath, expected_text):
    """
    Verify that an element identified by XPath contains the expected text.

    Args:
        context: Behave context
        xpath: XPath selector for the element
        expected_text: Expected text content
    """
    actual_text = context.page.get_element_text(xpath)
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in '{actual_text}'"


@step('I verify element page title contains text "{expected_text}"')
def verify_element_contains_text_with_pom(context, expected_text):
    login_page = LoginPage()
    actual_text = context.page.get_element_text(login_page.header)
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in '{actual_text}'"


@step('I wait for element "{xpath}" to be visible')
def wait_for_element(context, xpath):
    """
    Wait for an element identified by XPath to be visible.

    Args:
        context: Behave context
        xpath: XPath selector for the element
    """
    context.page.wait_for_element(xpath)


@step('Login with following credentials')
def login_with_credentials(context):
    for row in context.table:
        username = row['username']
        password = row['password']

        if username != 'Skip':
            context.page.fill_element("//input[@name='username']", username)

        if password != 'Skip':
            context.page.fill_element("//input[@name='password']", password)

        context.page.click_element("//button[text()=' Login ']")


@step('Login with following credentials from table')
def login_with_credentials_from_table(context):
    """
    Logs in using the defined credentials from a table provided within the test context.
    'username' - User name
    'password' - password
    'address' - Address (optional)

    If 'username' or 'password' is 'Skip', the corresponding field will be skipped.
    """
    username = None
    password = None

    for row in context.table:
        key = row[0]
        value = row[1]

        if key == 'username':
            username = value
        elif key == 'password':
            password = value

    if username and username != 'Skip':
        context.page.fill_element("//input[@name='username']", username)

    if password and password != 'Skip':
        context.page.fill_element("//input[@name='password']", password)

    context.page.click_element("//button[text()=' Login ']")


@step('I login as "{user_type}"')
def login_as_user(context, user_type):
    """
    Args:
        user_type: Type of user to login as
        context (behave.runner.Context):
    """
    # if user_type == 'user':
    #     user_name = 'pcs.automationclass@gmail.com'
    #     password = '1234567'
    # elif user_type == 'admin':
    #     user_name = 'admin@gmail.com'
    #     password = 'admin1234'
    # else:
    #     user_name = 'pcs.automationclass@gmail.com'
    #     password = 'xxxxxx'

    user_credentials = {
        "user": ("pcs.automationclass@gmail.com", "1234567"),
        "admin": ("pcs.automationclass@gmail.com", "xxxxxx")
    }

    # fill username
    # user_name_xpath = "//input[@name='username']"
    user_name_xpath = LoginPage().username
    # fill_text_in_element(context, user_name, user_name_xpath)
    fill_text_in_element(context, user_credentials[user_type][0], user_name_xpath)
    # fill password
    # password_xpath = "//input[@name='password']"
    password_xpath = LoginPage().password
    # fill_text_in_element(context, password, password_xpath)
    fill_text_in_element(context, user_credentials[user_type][1], password_xpath)
    # Click button
    # login_button_xpath = "//button[text()=' Login ']"
    login_button_xpath = LoginPage().login_button
    click_on_element(context, login_button_xpath)
