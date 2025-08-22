from behave import step

@step('kd I click on "{xpath}"')
def on_click(context, xpath):
    """
    Click on an element identified by XPath.

    :param context: Behave context
    :param xpath: XPath selector for the element
    """
    context.page.click_element(xpath)