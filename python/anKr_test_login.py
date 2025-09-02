from login_page import LoginPage
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

valid_app_url = "dev.linkmygear.com"
# page.goto("dev.linkmyger.com) replaced with page.goto(valid_app_url)

def test_login_success():
    page.goto(valid_app_url)
    login_page = LoginPage(page)
    login_page.login("mymail", "mypassword")
    assert login_page.verify_login_success()

def test_login_fail():
    page.goto(valid_app_url)
    login_page = LoginPage(page)
    login_page.login("mymail", "mywrongpassword")
    assert login_page.verify_login_success()

def test_login_fail2():
    page.goto(valid_app_url)
    login_page = LoginPage(page)
    login_page.login("mywrongmail", "mypassword")
    assert login_page.verify_login_fail()

def test_login_fail3():
    page.goto(valid_app_url)
    login_page = LoginPage(page)
    login_page.login(None, "mypassword")
    assert login_page.verify_login_fail()

def test_login_fail4():
    page.goto(valid_app_url)
    login_page = LoginPage(page)
    login_page.login("mymail", None)
    assert login_page.verify_login_fail()
