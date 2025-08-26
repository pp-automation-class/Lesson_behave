from behave import step


@step('Ankr login as "{user_type}"')
def ankr_login_as_user(context, user_type):
    """
    Args:
        user_type: Type of user to login as
        context (behave.runner.Context):
    """
    if user_type == 'user':
        user_name = 'akr.autotest@gmail.com'
        password = '12345'
    elif user_type == 'admin':
        user_name = 'admin@gmail.com'
        password = 'admin1234'
    else:
        user_name = 'autotest@gmail.com'
        password = '13579'



    # fill username
    def fill_text_in_element(context, text, xpath):
        if text != 'Skip':
            context.page.fill_element(xpath, text)

    user_name_xpath = "//input[@name='username']"
    fill_text_in_element(context, user_name, user_name_xpath)
    # fill password
    password_xpath = "//input[@name='password']"
    fill_text_in_element(context, password, password_xpath)
    # Click login button

    def click_on_element(context, xpath):
        context.page.click_element(xpath)

    login_button_xpath = "//button[text()=' Login ']"
    click_on_element(context, login_button_xpath)
