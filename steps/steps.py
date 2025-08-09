"""
Step definitions for web interactions using the Lingh framework.
"""

from behave import step


@step('I navigate to "{url}"')
def navigate_to_url(context, url):
    """
    Navigate to a URL.
    
    Args:
        context: Behave context
        url: URL to navigate to
    """
    if url == 'https://dev.linkmygear.com':
        url = 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com'
    context.page.navigate(url)


@step('I click on "{xpath}"')
def click_on_element(context, xpath):
    """
    Click on an element identified by XPath.
    
    Args:
        context: Behave context
        xpath: XPath selector for the element
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