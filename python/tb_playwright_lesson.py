from playwright.sync_api import sync_playwright

# browsers = ["chromium", "firefox"]

browsers = ["chromium"]

for browser_type in browsers:
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False)
        else:
            browser = p.firefox.launch(headless=False)
        context_dev = browser.new_context()

        context_dev.tracing.start(name="trace", screenshots=True, snapshots=True)

        page_dev = context_dev.new_page()
        page_dev.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")

        # context_app = browser.new_context()
        # page_app = context_app.new_page()
        # page_app.goto("https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com")

        # page_dev.get_by_label("Sign in")
        # page_dev.get_by_text("Sign in")
        # page_dev.get_by_alt_text("Logo")
        #
        # page_dev.locator("div.dialog-off-canvas-main-canvas")
        #
        # page_dev.locator("//div[@class='dialog-off-canvas-main-canvas']")

        # page.wait_for_selector("//button1", timeout=3000)
        # page.wait_for_timeout(2000)
        username = page_dev.locator("//input[@name='username']")
        # username.fill("email")
        username.type("email", delay=500)
        # username.click()
        password = page_dev.locator("//input[@name='password']")
        password.fill("1234")
        page_dev.wait_for_timeout(2000)
        page_dev.keyboard.press("Enter")
        message = page_dev.text_content(".el-message__content")
        print("Received message:", message)

        forgot_password = page_dev.locator("//a[text()='Forgot password?']")
        forgot_password.click()
        page_dev.wait_for_timeout(3000)
        restore_text = page_dev.locator("text='Restore Password'")

        if restore_text.is_visible():
            print("You're on the right page.")
        else:
            print("Wrong page or something went wrong.")

        username2 = page_dev.locator("//input[@class='el-input__inner']")
        username2.click()
        username2.type("email", delay=500)
        username2.press("Enter")
        restore_text2 = page_dev.locator("text='Please enter you email address'")
        if restore_text.is_visible():
            print("Let's start again")
        back_to_login_page = page_dev.locator("//a[text()='Back to Login page']")
        back_to_login_page.click()
        page_dev.wait_for_timeout(3000)

        username = page_dev.locator("//input[@name='username']")
        username.fill("email2")
        page_dev.wait_for_timeout(2000)
        password = page_dev.locator("//input[@name='password']")
        password.fill("<241324")
        page_dev.wait_for_timeout(2000)

        logo = page_dev.locator(".logo")
        logo.click()

        new_account = page_dev.locator("//a[text()='Create an account']")
        new_account.click()

        # Fill in the email
        username3 = page_dev.locator("//input[@class='el-input__inner']")
        username3.fill("new_email@mail.com")

        # Click the visible part of the checkbox (not the input!)
        checkbox_visual = page_dev.locator("//span[contains(@class, 'el-checkbox__inner')]")
        checkbox_visual.click()

        # Wait a little for state change to register
        page_dev.wait_for_timeout(500)

        # Locate the real checkbox input (used only to check if it’s selected)
        checkbox = page_dev.locator("//input[@type='checkbox']")

        # Check if the checkbox is now checked
        if checkbox.is_checked():
            print("✅ Checkbox is checked.")
            new_register = page_dev.locator("//input[contains(@class, 'lmg-btn')]")
            new_register.click()
            print("Thank you for your time.")
        else:
            print("❌ Checkbox is NOT checked.")
            # Try clicking the visual checkbox again
            checkbox_visual.click()
            page_dev.wait_for_timeout(300)
            if checkbox.is_checked():
                print("✅ Checkbox is now checked.")
                new_register = page_dev.locator("//button[contains(@class, 'lmg-btn--sm')]")
                new_register.click()
                print("Thank you for your time.")
            else:
                print("❌ Still not checked. Something is wrong.")

        browser.close()
