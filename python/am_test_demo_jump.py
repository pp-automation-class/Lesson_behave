import logging
import datetime

from playwright.sync_api import sync_playwright

from pages.am_login_page import LoginPage


def goto_demo_jump_page():
    page.locator("//button[contains(.,'Demo Jump')]").click()
    page.wait_for_selector("//div/h3[@class='modal-title' and .='Generate demo jump']")


def screenshot():
    screenshot_path = f"../../temp/demo_jump{datetime.datetime.now().strftime('%Y-%m-%d %H%M%S%f')}.png"
    page.screenshot(path=screenshot_path, full_page=True)
    logging.info(f"Screenshot saved to {screenshot_path}")


def test_demo_jump_success():
    logging.info("Test: Generate demo jump - success case")
    goto_demo_jump_page()
    page.click("//input[@placeholder='Select date and time']")
    page.click("//div[@class='el-picker-panel__footer']/button[.='OK']")
    page.click(
        "//div[@class='form-submit']/button/span[contains(.,'Generate demo jump')]"
    )
    if login_page.element_exists(
        "//p[@class='el-message__content' and .='Demo device jumps limit exceeded.']",
        timeout=2000,
    ):
        page.wait_for_timeout(2000)
        screenshot()
        error = "Demo device jumps limit exceeded."
        raise Exception(error)

    page.wait_for_selector(
        "//p[@class='el-message__content' and .='Demo jump has been generated']",
        timeout=15000,
    )
    logging.info("Passed: Demo jump has been generated")
    screenshot()


def test_demo_jump_cancel():
    logging.info("Test: Generate demo jump - cancel case")
    goto_demo_jump_page()
    page.click("//button[@class='modal-close']")
    page.wait_for_selector("//h3[contains(text(), 'My device')]")
    logging.info("Passed: Generate demo jump has been canceled")


def test_demo_jump_fail_empty_date():
    page.wait_for_timeout(4000)
    logging.info("Test: Generate demo jump - fail case - empty date")
    goto_demo_jump_page()
    page.click(
        "//div[@class='form-submit']/button/span[contains(.,'Generate demo jump')]"
    )
    page.wait_for_selector(
        "//div[@class='el-form-item__error' and contains(.,'Please select date and time')]"
    )
    logging.info(
        "Passed: Validation message is displayed - Please select date and time"
    )
    screenshot()


logging.basicConfig(
    filename="../../temp/test_demo_jump.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()

if __name__ == "__main__":
    try:
        logging.info("Starting test_demo_jump.py")
        logging.info("Login to linkmygear.com")
        login_page = LoginPage(page)
        login_page.navigate().login("7nxjno9lr@mozmail.com", "r+WLLX9qwx^:>:3")
        assert login_page.verify_login_success(), "Can't continue: Login failed"

        test_demo_jump_success()
        test_demo_jump_cancel()
        test_demo_jump_fail_empty_date()
    except Exception as error:
        logging.error(error)
        raise error
    finally:
        context.close()
        browser.close()
        p.stop()

        logging.info("Ending test_demo_jump.py")
