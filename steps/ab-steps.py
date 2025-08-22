from behave import step

@step('AB I click on "{xpath}"')
def ab_click_on_element(context, xpath):
    """
    Click on an element identified by XPath.

    :param context: Behave context
    :param xpath: XPath selector for the element
    """
    context.page.click_element(xpath)
