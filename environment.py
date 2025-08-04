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


def before_scenario(context, scenario):
    """
    Initialize a new browser instance before each scenario.
    
    Args:
        context: Behave context
        scenario: Behave scenario
    """
    # Create a new browser instance
    context.browser = Browser()
    context.browser.launch()
    
    # Create a page object
    context.page = Page(context.browser.get_page())


def after_scenario(context, scenario):
    """
    Close the browser after each scenario.
    
    Args:
        context: Behave context
        scenario: Behave scenario
    """
    if hasattr(context, "browser"):
        context.browser.close()
