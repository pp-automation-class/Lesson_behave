"""
Behave environment hooks for the Lingh framework.
"""

from browser import Browser
from page import Page


def before_all(context):
    """
    Initialize the browser before all scenarios.
    
    Args:
        context: Behave context
    """
    # Set default browser configuration
    context.browser_type = getattr(context.config, "browser", "chromium")
    context.headless = getattr(context.config.userdata, "headless", "true").lower() == "true"
    # print("before_all")

# def before_feature(context, feature):
#     print("before_feature")

def before_scenario(context, scenario):
    """
    Initialize a new browser instance before each scenario.
    
    Args:
        context: Behave context
        scenario: Behave scenario
    """
    # Create a new browser instance
    # print("before_scenario")
    context.browser = Browser()
    context.browser.launch()
    
    # Create a page object
    context.page = Page(context.browser.get_page())

# def before_step(context, step):
#     print("before_step")
#
# def after_step(context, step):
#     print("after_step")

def after_scenario(context, scenario):
    """
    Close the browser after each scenario.
    
    Args:
        context: Behave context
        scenario: Behave scenario
    """
    # print("after_scenario")
    if hasattr(context, "browser"):
        context.browser.close()

# def after_feature(context, feature):
#     print("after_feature")
#
# def after_all(context):
#     print("after_all")
