from login_page import LoginPage
from devices_page import DevicesPage

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()


def test_open_news():
    page.goto("dev.linkmyger.com")
    login_page = LoginPage(page)
    login_page.login("mymail", "mypassword")
    login_page.verify_login_success()
    devices_page = DevicesPage(page)
    devices_page.go_to_news()
    devices_page.verify_on_news_page()


