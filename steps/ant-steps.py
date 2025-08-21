from behave import step


@step('ANT I login as "{user_type}"')
def ant_login_as_tester(context, user_type):
    """
    Args:
        user_type: Type of user
        context (behave.runner.Context):
    """

    if user_type == 'tester':
        user_name = 'anton.bondarenko.test@gmail.com'
        password = '123459'
    elif user_type == 'admin':
        user_name = 'admin@gmail.com'
        password = '7654321'
    else:
        user_name = 'anton.bondarenko.test@gmail.com'
        password = '123xxx'

    # fill tester username
    def fill_text_in_element(context, text, xpath):
        if text != 'Skip':
            context.page.fill_element(xpath, text)

    user_name_xpath = "//input[@name='username']"
    fill_text_in_element(context, user_name, user_name_xpath)
    # fill tester password
    password_xpath = "//input[@name='password']"
    fill_text_in_element(context, password, password_xpath)
    # click login button

    def click_on_element(context, xpath):
        context.page.click_element(xpath)

    login_button_xpath = "//button[text()=' Login ']"
    click_on_element(context, login_button_xpath)


@step('ANT I add new device "{device_name}"')
def ant_add_new_device(context, device_name):
    # click add device button
    def click_on_element(context, xpath):
        context.page.click_element(xpath)
    element_xpath = "//button[.//span[text()='Add new device']]"
    click_on_element(context, element_xpath)

    # wait for element visible
    element_xpath = "//h3[@class='modal-title' and text()='Add device']"

    def wait_for_element(context, xpath):
        context.page.wait_for_element(xpath)
    wait_for_element(context, element_xpath)

    # select devise type
    element_xpath = "//label[text()='Device type']"
    click_on_element(context, element_xpath)

    element_xpath = "//li[.//span[text()='Airguard other']]"
    click_on_element(context, element_xpath)

    # fill device name
    def fill_text_in_element(context, text, xpath):
        if text != 'Skip':
            context.page.fill_element(xpath, text)

    element_xpath = "//input[@class='el-input__inner']"
    fill_text_in_element(context, device_name, element_xpath)

    # click add new device button
    element_xpath = "//div[@class='form-submit']/button[.//span[text()='Add new device']]"
    click_on_element(context, element_xpath)


@step('ANT I delete "{device_name}"')
def ant_delete_device(context, device_name):
    # click delete button
    def click_on_element(context, xpath):
        context.page.click_element(xpath)
    element_xpath = f"//tr[@class='el-table__row' and .//span[text()='{device_name}']]//button[text()=' Delete ']"
    click_on_element(context, element_xpath)

    # wait for element visible
    element_xpath = "//h3[@class='modal-title' and text()='Delete device']"

    def wait_for_element(context, xpath):
        context.page.wait_for_element(xpath)
    wait_for_element(context, element_xpath)

    # confirm delete
    element_xpath = "//button[text()='Delete']"
    click_on_element(context, element_xpath)

    # verify device delete confirmation message
    def verify_element_exists(context, xpath):
        context.page.verify_element_exists(xpath)

    element_xpath = "//*[contains(@class, 'el-message__content') and contains(text(), 'Device deleted')]"
    verify_element_exists(context, element_xpath)
