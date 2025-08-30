
from behave import step
from pages.login import LoginPage


@step('anKr I navigate to "{url}"')
def ankr_navigete_to_url(context, url):
    if url == 'https://dev.linkmygear.com':
        url = 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com'
    context.page.navigate(url)
    print(f"Navigated to {url}")


@step('anKr I navigate to "{env}" environment')
def ankr_navigate_to_env(context, env):
    """
    Navigate to an environment (`dev`, `prod`).
    """
    environments = {
        'dev': 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com',
        'prod': 'https://app.linkmygear.com'
    }
    context.page.navigate(environments[env])


@step('anKr click on "{xpath}"')
def ankr_click_on_element(context, xpath):
    """
    Click on an element identified by XPath.

    :param context: Behave context
    :param xpath: XPath selector for the element
    """
    context.page.click_element(xpath)
    print(f"Clicked element: {xpath}")


@step('anKr fill "{text}" in element "{xpath}"')
def ankr_fill_in_element(context, text, xpath):
    """
    Fill text in an element identified by XPath.

    Args:
        context: Behave context
        text: Text to fill in the element
        xpath: XPath selector for the element
    """
    if text != 'Skip':
        context.page.fill_element(xpath, text)
        print(f"Filled '{text}' in {xpath}")


@step('anKr I verify element "{xpath}" exists')
def ankr_verify_element_exist(context, xpath):
    """
    Verify that an element identified by XPath exists.

    Args:
        context: Behave context
        xpath: XPath selector for the element
    """
    context.page.wait_for_element(xpath, timeout=10000)
    context.page.verify_element_exists(xpath)
    print(f"Verified element exists: {xpath}")


@step('anKr I verify element "{xpath}" contains text "{expected_text}"')
def ankr_verify_element_contains_text(context, xpath, expected_text):
    context.page.wait_for_element(xpath, timeout=5000)  # wait until element visible
    actual_text = context.page.get_element_text(xpath)
    print(f"Element {xpath} text: '{actual_text}'")
    assert expected_text in actual_text, f"Expected '{expected_text}', got '{actual_text}'"


@step('anKr I verify element page title contains text "{expected_text}"')
def ankr_verify_element_contains_text_with_pom(context, expected_text):
    login_page = LoginPage()
    actual_text = context.page.get_element_text(login_page.header)
    print(f"Header text is: {actual_text}")
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in '{actual_text}'"


@step('anKr I login as "{user_type}"')
def ankr_login_as_user(context, user_type):
    """
    Args:
        user_type: Type of user to login as
        context (behave.runner.Context):
    """
    #     if user_type == 'user':
    #         user_name = 'akr.autotest@gmail.com'
    #         password = '12345'
    #     elif user_type == 'admin':
    #         user_name = 'akr.autotest@gmail.com'
    #         password = '13579'
    #     else:
    #         user_name = 'akr.autotest@gmail.com'
    #         password = 'xxxxxx'

    user_credentials = {
        "user": {"username": "akr.autotest@gmail.com", "password": "12345"},
        "admin": {"username": "pcs.automationclass@gmail.com", "password": "13579"}
    }

    creds = user_credentials[user_type]

    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    login_button_xpath = "//button[text()=' Login ']"

    # Fill username field
    context.page.wait_for_element(username_xpath, timeout=5000)
    context.page.fill_element(username_xpath, creds["username"])
    print(f"Filled username: {creds['username']}")

    # Fill password field
    context.page.wait_for_element(password_xpath, timeout=5000)
    context.page.fill_element(password_xpath, creds["password"])
    print(f"Filled password: {creds['password']}")

    # Fill login button
    context.page.wait_for_element(login_button_xpath, timeout=5000)
    context.page.click_element(login_button_xpath)
    print(f"Clicked Login button for user type: {user_type}")

    # fill username
    # user_name_xpath = "//input[@name='username']"
    # # fill_text_in_element(context, user_name, user_name_xpath)
    # fill_text_in_element(context, user_credentials[user_type][0], user_name_xpath)
    #
    # # fill password
    # password_xpath = "//input[@name='password']"
    # # fill_text_in_element(context, password, password_xpath)
    # fill_text_in_element(context, user_credentials[user_type][1], password_xpath)

    # Click login button
    # def click_on_element(context, xpath):
    #     context.page.click_element(xpath)
    #
    # login_button_xpath =  "//button[text()=' Login ']"
    # click_on_element(context, login_button_xpath)
