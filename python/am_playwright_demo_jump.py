from playwright.sync_api import sync_playwright

from pages.am_login_page import LoginPage

with sync_playwright() as p:
    page = p.chromium.launch(headless=False).new_context().new_page()
    login_page = LoginPage(page)
    login_page.navigate().login("7nxjno9lr@mozmail.com", "r+WLLX9qwx^:>:3")
    assert login_page.verify_login_success()
