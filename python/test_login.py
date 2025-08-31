from login_page import LoginPage
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


def test_login_success():
    page.goto("dev.linkmyger.com")
    login_page = LoginPage(page)
    # login_page.input_username("mymail")
    # login_page.input_username("mypassword")
    # login_page.click_login()
    login_page.login("mymail", "mypassword")
    assert login_page.verify_login_success()


def test_login_fail():
    page.goto("dev.linkmyger.com")
    login_page = LoginPage(page)
    login_page.login("mymail", "mywrongpassword")
    assert login_page.verify_login_fail()


def test_login_fail_2():
    page.goto("dev.linkmyger.com")
    login_page = LoginPage(page)
    login_page.login(None, "mywrongpassword")
    assert login_page.verify_login_fail()


def test_login_fail_3():
    page.goto("dev.linkmyger.com")
    login_page = LoginPage(page)
    login_page.login("my mail", None)
    assert login_page.verify_login_fail()
