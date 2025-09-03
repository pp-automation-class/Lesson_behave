import logging

from playwright.sync_api import sync_playwright

from pages.am_login_page import LoginPage
from python.am_utils import element_exists, screenshot, log_files_path

SECTION_NAME = "test_demo_jump"


def goto_demo_jump_page():
    page.locator("//button[contains(.,'Demo Jump')]").click()
    page.wait_for_selector("//div/h3[@class='modal-title' and .='Generate demo jump']")


def test_demo_jump_success():
    logging.info("Test: Generate demo jump - success case")
    goto_demo_jump_page()
    page.click("//input[@placeholder='Select date and time']")
    page.click("//div[@class='el-picker-panel__footer']/button[.='OK']")
    page.click(
        "//div[@class='form-submit']/button/span[contains(.,'Generate demo jump')]"
    )
    if element_exists(
        page,
        "//p[@class='el-message__content' and .='Demo device jumps limit exceeded.']",
        timeout=2000,
    ):
        page.wait_for_timeout(2000)
        screenshot(page, SECTION_NAME)
        error = "Demo device jumps limit exceeded."
        raise Exception(error)

    page.wait_for_selector(
        "//p[@class='el-message__content' and .='Demo jump has been generated']",
        timeout=15000,
    )
    logging.info("Passed: Demo jump has been generated")
    screenshot(page, SECTION_NAME)


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
    screenshot(page, SECTION_NAME)


logging.basicConfig(
    filename=log_files_path(SECTION_NAME + ".log"),
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()

logging.info("Starting "+SECTION_NAME)

try:
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

    logging.info("Ending "+SECTION_NAME)
