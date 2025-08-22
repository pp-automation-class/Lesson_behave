

from behave import step


@step('User navigates to "{url}"')
def user_navigate_to_url(context, url):
    if url == 'https://dev.linkmygear.com':
        url = 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com'
    context.page.navigate(url)


@step('User verify element "{xpath}" contains text "{expected_text}"')
def user_verify_element_contains_text(context, xpath, expected_text):
    """
    Verify that an element identified by XPath contains the expected text.

    Args:
        context: Behave context
        xpath: XPath selector for the element
        expected_text: Expected text content
    """
    actual_text = context.page.get_element_text(xpath)
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in '{actual_text}'"