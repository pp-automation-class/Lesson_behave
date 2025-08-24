from behave import step
from steps import fill_text_in_element, click_on_element, wait_for_element,verify_element_exists


class AntLoginPage:

    def __init__(self):
        self.user_name = "//input[@name='username']"
        self.password = "//input[@name='password']"
        self.login_button = "//button[text()=' Login ']"

class AntDevicePage:

    def __init__(self):
        self.add_new_device = "//button[.//span[text()='Add new device']]"
        self.add_device = "//h3[@class='modal-title' and text()='Add device']"
        self.device_type = "//label[text()='Device type']"
        self.device_airguard = "//li[.//span[text()='Airguard other']]"
        self.device_name_field = "//input[@class='el-input__inner']"
        self.add_new_device_button =  "//div[@class='form-submit']/button[.//span[text()='Add new device']]"



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
    user_name_xpath = AntLoginPage().user_name
    fill_text_in_element(context, user_name, user_name_xpath)
    # fill tester password
    password_xpath = AntLoginPage().password
    fill_text_in_element(context, password, password_xpath)
    # click login button
    login_button_xpath = AntLoginPage().login_button
    click_on_element(context, login_button_xpath)


@step('ANT I add new device "{device_name}"')
def ant_add_new_device(context, device_name):
    element_xpath = AntDevicePage().add_new_device
    click_on_element(context, element_xpath)

    # wait for element visible
    element_xpath = AntDevicePage().add_device
    wait_for_element(context, element_xpath)

    # select devise type
    element_xpath = AntDevicePage().device_type
    click_on_element(context, element_xpath)

    element_xpath = AntDevicePage().device_airguard
    click_on_element(context, element_xpath)

    # fill device name
    element_xpath = AntDevicePage().device_name_field
    fill_text_in_element(context, device_name, element_xpath)

    # click add new device button
    element_xpath = AntDevicePage().add_new_device_button
    click_on_element(context, element_xpath)


@step('ANT I delete "{device_name}"')
def ant_delete_device(context, device_name):
    # click delete button
    element_xpath = f"//tr[@class='el-table__row' and .//span[text()='{device_name}']]//button[text()=' Delete ']"
    click_on_element(context, element_xpath)

    # wait for element visible
    element_xpath = "//h3[@class='modal-title' and text()='Delete device']"
    wait_for_element(context, element_xpath)

    # confirm delete
    element_xpath = "//button[text()='Delete']"
    click_on_element(context, element_xpath)

    # verify device delete confirmation message
    element_xpath = "//*[contains(@class, 'el-message__content') and contains(text(), 'Device deleted')]"
    verify_element_exists(context, element_xpath)
