import uuid

from playwright.sync_api import sync_playwright


def login_linkmygear(browser, username:str, password:str):
    context = browser.new_context()

    context.tracing.start(name="trace", screenshots=True, snapshots=True)

    page = context.new_page()
    page.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
    page.wait_for_selector("//h5[.='Login to Your Account']", timeout=3000)

    page.locator("//input[@name='username']").fill(username)

    page.locator("//input[@name='password']").fill(password)

    page.locator("//button").click()

    page.wait_for_timeout(2000)

    unique = str(uuid.uuid4())
    page.screenshot(path=f"C:\\Users\\aamal\\Pictures\\Screenshots\\Chromium_dev_linkmygear_{unique}.png")
    context.tracing.stop(path=f"C:\\Users\\aamal\\PycharmProjects\\Temp\\trace_{unique}.zip")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    login_linkmygear(browser, username="7nxjno9lr@mozmail.com", password="r+WLLX9qwx^:>:3")

    login_linkmygear(browser, username="email@email.com", password="1234")


    browser.close()
