import uuid

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    context.tracing.start(name="trace", screenshots=True, snapshots=True)

    page = context.new_page()
    page.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")
    page.wait_for_selector("//h5[.='Login to Your Account']", timeout=3000)

    page.locator("//input[@name='username']").fill("email@email.com")

    page.locator("//input[@name='password']").fill("1234")

    page.locator("//button").click()

    page.wait_for_timeout(2000)

    unique = str(uuid.uuid4())
    page.screenshot(path=f"C:\\Users\\aamal\\Pictures\\Screenshots\\Chromium_dev_linkmygear_{unique}.png")
    context.tracing.stop(path=f"C:\\Users\\aamal\\PycharmProjects\\Temp\\trace_{unique}.zip")

    browser.close()
