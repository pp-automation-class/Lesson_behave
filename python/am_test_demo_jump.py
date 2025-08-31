from playwright.sync_api import sync_playwright

from pages.am_login_page import LoginPage


def goto_demo_jump_page():
    page.locator("//button[contains(.,'Demo Jump')]").click()
    page.wait_for_selector("//div/h3[@class='modal-title' and .='Generate demo jump']")


def test_demo_jump_success():
    goto_demo_jump_page()
    page.click("//input[@placeholder='Select date and time']")
    page.click("//div[@class='el-picker-panel__footer']/button[.='OK']")
    page.click(
        "//div[@class='form-submit']/button/span[contains(.,'Generate demo jump')]"
    )
    page.wait_for_timeout(5000)
    page.wait_for_selector(
        "//p[@class='el-message__content' and .='Demo jump has been generated']"
    )
    page.wait_for_timeout(3000)


def test_demo_jump_cancel():
    goto_demo_jump_page()
    page.click("//button[@class='modal-close']")
    page.wait_for_selector("//h3[contains(text(), 'My device')]")
    page.wait_for_timeout(3000)


def test_demo_jump_fail_empty_date():
    goto_demo_jump_page()
    page.click(
        "//div[@class='form-submit']/button/span[contains(.,'Generate demo jump')]"
    )
    page.wait_for_selector(
        "//div[@class='el-form-item__error' and contains(.,'Please select date and time')]"
    )
    page.wait_for_timeout(3000)


p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()

if __name__ == "__main__":
    try:
        login_page = LoginPage(page)
        login_page.navigate().login("7nxjno9lr@mozmail.com", "r+WLLX9qwx^:>:3")
        assert login_page.verify_login_success(), "Can't continue: Login failed"

        test_demo_jump_success()
        test_demo_jump_cancel()
        test_demo_jump_fail_empty_date()

    finally:
        context.close()
        browser.close()
        p.stop()
