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
