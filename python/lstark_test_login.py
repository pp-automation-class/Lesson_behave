
DEV_LINKMYGER_COM = "https:dev.linkmyger.com"

from  lstark_login_page import LstarkLoginPage

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

def test_login_success():
    page.goto(DEV_LINKMYGER_COM )
    login_page = LstarkLoginPage(page)
    # login_page.input_username("myemail")
    # login_page.input_username("mypassword")
    # login_page.click_login()
    login_page.login("myemail", "mypassword")
    assert login_page.verify_login_success()

def test_login_fail():
    page.goto(DEV_LINKMYGER_COM )
    login_page = LstarkLoginPage(page)
    login_page.login("myemail", "mywrongpassword")
    assert login_page.verify_login_fail()

def test_login_fail2():
    page.goto(DEV_LINKMYGER_COM )
    login_page = LstarkLoginPage(page)
    login_page.login(None, "mywrongpassword")
    assert login_page.verify_login_fail()

def test_login_fail3():
    page.goto(DEV_LINKMYGER_COM )
    login_page = LstarkLoginPage(page)
    login_page.login("myemail", None)
    assert login_page.verify_login_fail()

# page.goto("dev.linkmyger.com) replaced with page.goto(DEV_LINKMYGER_COM )
# DEV_LINKMYGER_COM  - is constant variable



