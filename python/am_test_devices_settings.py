import logging

from playwright.sync_api import sync_playwright

from pages.am_login_page import LoginPage
from python.am_utils import screenshot, random_username, log_files_path

SECTION_NAME = "test_devices_settings"
device_name = "Test Device " + random_username()


def test_devices_settings_background():
    logging.info("Login to linkmygear.com")
    login_page = LoginPage(page)
    login_page.navigate().login("7nxjno9lr@mozmail.com", "r+WLLX9qwx^:>:3")
    assert login_page.verify_login_success(), "Can't continue: Login failed"
    page.locator("//a[@href='#/device-settings']").click()
    page.wait_for_selector(
        "//div[@class='row']/h3[contains(text(), 'Devices Settings')]"
    )


def test_devices_settings_add_new_device():
    logging.info(f"Test: Device Settings - Add New Device '{device_name}'")
    page.click("//button[.//span[text()='Add new device']]")
    page.wait_for_selector("//h3[@class='modal-title' and text()='Add device']")
    page.click("//label[text()='Device type']")
    page.click("//li[.//span[text()='Airguard other']]")
    page.fill("//input[@class='el-input__inner']", device_name)
    page.click("//div[@class='form-submit']/button[.//span[text()='Add new device']]")
    page.wait_for_timeout(2000)
    logging.info("Passed: Device Settings - New Device Added")
    screenshot(page, SECTION_NAME)


def tests_device_settings_edit_device_and_update():
    logging.info(
        f"Test: Device Settings - Edit Device: rename from '{device_name}' to '{device_name+" #2"}'"
    )
    page.wait_for_selector("(//div/span[text()='" + device_name + "'])[1]")
    page.click(
        "(//span[text()='"
        + device_name
        + "'])[1]/../../../td[4]/div/div[@class='btns']/button[.=' Edit ']"
    )
    page.wait_for_selector("//h3[@class='modal-title' and text()='Edit device']")
    page.fill("//input[@class='el-input__inner']", value=device_name + " #2")
    page.click("//div[@class='form-submit']/button[.//span[text()='Update']]")
    page.wait_for_timeout(2000)
    logging.info("Passed: Device Settings - Device Edited")
    screenshot(page, SECTION_NAME)


def tests_device_settings_delete_device():
    logging.info(f"Test: Device Settings - Delete Device '{device_name+" #2"}'")
    page.wait_for_selector("(//div/span[text()='" + device_name + " #2" + "'])[1]")
    page.click(
        "(//span[text()='"
        + device_name
        + " #2"
        + "'])[1]/../../../td[4]/div/div[@class='btns']/button[.=' Delete ']"
    )
    page.wait_for_selector("//h3[@class='modal-title' and text()='Delete device']")
    page.click("//button[.='Delete']")
    page.wait_for_timeout(2000)
    logging.info("Passed: Device Settings - Device Deleted")
    screenshot(page, SECTION_NAME)


logging.basicConfig(
    filename=log_files_path(SECTION_NAME + ".log"),
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.info("Starting " + SECTION_NAME)

play = sync_playwright().start()
browser = play.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()


try:
    test_devices_settings_background()

    test_devices_settings_add_new_device()

    tests_device_settings_edit_device_and_update()

    tests_device_settings_delete_device()

except Exception as error:
    logging.error(error)
    raise error
finally:
    context.close()
    browser.close()
    play.stop()

    logging.info("Ending " + SECTION_NAME)
