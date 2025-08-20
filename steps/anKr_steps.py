from behave import step

@step('I login as "{user_type}"')
def login_as_anKr_user(context, user_type):
    """
    Args:
        user_type: Type of user to login as
        context (behave.runner.Context):
    """
    # if user_type == 'user':
    #     user_name = 'akr.autotest@gmail.com'
    #     password = '12345'
    # elif user_type == 'admin':
    #     user_name = 'admin@gmail.com'
    #     password = 'admin1234'
    # else:
    #     user_name = 'autotest@gmail.com'
    #     password = '13579'


    user_credentials = {
        "user": ("akr.autotest@gmail.com", "12345"),
        "admin": ("akr.autotest@gmail.com", "xxxxxx")
    }

    # fill username
    user_name_xpath = "//input[@name='username']"
    # fill_text_in_element(context, user_name, user_name_xpath)
    fill_text_in_element(context, user_credentials[user_type][0], user_name_xpath)
    # fill password
    password_xpath = "//input[@name='password']"
    # fill_text_in_element(context, password, password_xpath)
    fill_text_in_element(context, user_credentials[user_type][1], password_xpath)
    # Click button
    login_button_xpath = "//button[text()=' Login ']"
    click_on_element(context, login_button_xpath)