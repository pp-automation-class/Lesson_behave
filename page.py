"""
Page object module for the Lingh framework.
"""

from playwright.sync_api import Page as PlaywrightPage


class Page:
    """
    Page class to interact with web pages.
    """
    
    def __init__(self, page: PlaywrightPage):
        """
        Initialize the page.
        
        Args:
            page (PlaywrightPage): Playwright page instance
        """
        self.page = page
    
    def click_element(self, xpath):
        """
        Click on an element identified by XPath.
        
        Args:
            xpath (str): XPath selector for the element
        """
        self.page.click(f"xpath={xpath}")
    
    def fill_element(self, xpath, text):
        """
        Fill text in an element identified by XPath.
        
        Args:
            xpath (str): XPath selector for the element
            text (str): Text to fill in the element
        """
        self.page.fill(f"xpath={xpath}", text)
    
    def element_exists(self, xpath, timeout=5000):
        """
        Check if an element identified by XPath exists.
        
        Args:
            xpath (str): XPath selector for the element
            timeout (int): Timeout in milliseconds
            
        Returns:
            bool: True if the element exists, False otherwise
        """
        try:
            self.page.wait_for_selector(f"xpath={xpath}", timeout=timeout)
            return True
        except:
            return False
    
    def verify_element_exists(self, xpath, timeout=5000):
        """
        Verify that an element identified by XPath exists.
        Raises an assertion error if the element does not exist.
        
        Args:
            xpath (str): XPath selector for the element
            timeout (int): Timeout in milliseconds
        """
        assert self.element_exists(xpath, timeout), f"Element with XPath '{xpath}' does not exist"
    
    def get_element_text(self, xpath):
        """
        Get the text content of an element identified by XPath.
        
        Args:
            xpath (str): XPath selector for the element
            
        Returns:
            str: Text content of the element
        """
        return self.page.text_content(f"xpath={xpath}")
    
    def wait_for_element(self, xpath, timeout=5000):
        """
        Wait for an element identified by XPath to be visible.
        
        Args:
            xpath (str): XPath selector for the element
            timeout (int): Timeout in milliseconds
            
        Returns:
            ElementHandle: The element handle
        """
        return self.page.wait_for_selector(f"xpath={xpath}", timeout=timeout)
    
    def navigate(self, url):
        """
        Navigate to a URL.
        
        Args:
            url (str): URL to navigate to
        """
        self.page.goto(url)