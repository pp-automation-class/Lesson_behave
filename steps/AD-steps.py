

from behave import step


@step('User navigates to "{url}"')
def ad_navigate_to_url(context, url):
    if url == 'https://dev.linkmygear.com':
        url = 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com'
    context.page.navigate(url)


@step('User verify element "{xpath}" contains text "{expected_text}"')
def ad_verify_element_contains_text(context, xpath, expected_text):
    """
    Verify that an element identified by XPath contains the expected text.

    Args:
        context: Behave context
        xpath: XPath selector for the element
        expected_text: Expected text content
    """
    actual_text = context.page.get_element_text(xpath)
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in '{actual_text}'"


@step('User fill "{text}" in element "{xpath}"')
def ad_fill_text_in_element(context, text, xpath):
    """
    Fill text in an element identified by XPath.

    Args:
        context: Behave context
        text: Text to fill in the element
        xpath: XPath selector for the element
    """
    if text != 'Skip':
        context.page.fill_element(xpath, text)


@step('User click on "{xpath}"')
def ad_click_on_element(context, xpath):
    """
    Click on an element identified by XPath.

    :param context: Behave context
    :param xpath: XPath selector for the element
    """
    context.page.click_element(xpath)


@step('User verify element "{xpath}" exists')
def ad_verify_element_exists(context, xpath):
    """
    Verify that an element identified by XPath exists.

    Args:
        context: Behave context
        xpath: XPath selector for the element
    """
    context.page.verify_element_exists(xpath)


@step('User navigate to "{url}"')
def ad_navigate_to_url(context, url):
    if url == 'https://dev.linkmygear.com':
        url = 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com'
    context.page.navigate(url)
