"""
Browser management module for the Lingh framework.
"""

from playwright.sync_api import sync_playwright, Browser as PlaywrightBrowser, Page as PlaywrightPage


class Browser:
    """
    Browser class to manage Playwright browser instances.
    """
    
    def __init__(self):
        """
        Initialize the browser.
        
        Args:
            browser_type (str): Type of browser to use (chromium, firefox, webkit)
            headless (bool): Whether to run the browser in headless mode
        """
        self.browser_type = "chromium"
        self.headless = False
        self.playwright = None
        self.browser_instance = None
        self.context = None
        self.page_instance = None
    
    def launch(self):
        """
        Launch the browser.
        
        Returns:
            PlaywrightBrowser: The browser instance
        """
        self.playwright = sync_playwright().start()
        
        if self.browser_type == "chromium":
            self.browser_instance = self.playwright.chromium.launch(headless=self.headless)
        elif self.browser_type == "firefox":
            self.browser_instance = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_type == "webkit":
            self.browser_instance = self.playwright.webkit.launch(headless=self.headless)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        
        self.context = self.browser_instance.new_context()
        self.page_instance = self.context.new_page()
        
        return self.browser_instance
    
    def get_page(self) -> PlaywrightPage:
        """
        Get the current page.
        
        Returns:
            PlaywrightPage: The current page
        """
        if not self.page_instance:
            self.launch()
        return self.page_instance
    
    def navigate(self, url):
        """
        Navigate to a URL.
        
        Args:
            url (str): URL to navigate to
        """
        self.get_page().goto(url)
    
    def close(self):
        """
        Close the browser.
        """
        if self.context:
            self.context.close()
        if self.browser_instance:
            self.browser_instance.close()
        if self.playwright:
            self.playwright.stop()