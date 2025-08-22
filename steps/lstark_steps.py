
from behave import step

@step('lstark I login as "{user_type}"')
def lstark_login_as_user(context, user_type):
    """
    Args:
        user_type: Type of user to login as
        context (behave.runner.Context):
    """
    # if user_type == 'user':
    #     user_name = 'lauravstesting53@gmail.com'
    #     password = 'T8st8ng38!'
    # elif user_type == 'admin':
    #     user_name = 'pcs.automationclass@gmail.com'
    #     password = '1234567'
    # else:
    #     user_name = 'pcs.automationclass@gmail.com'
    #     password = 'xxxxxx'

    user_credentials = {
        "user": ("lauravstesting53@gmail.com", "T8st8ng38!"),
        "admin": ("pcs.automationclass@gmail.com", "1234567")
    }


    # fill username
    def fill_text_in_element(context, text, xpath):
        if text != 'Skip':
            context.page.fill_element(xpath, text)

    user_name_xpath = "//input[@name='username']"
    #fill_text_in_element(context, user_name, user_name_xpath)
    fill_text_in_element(context,user_credentials[user_type][0], user_name_xpath)

    # fill password
    password_xpath = "//input[@name='password']"
    #fill_text_in_element(context, password, password_xpath)
    fill_text_in_element(context, user_credentials[user_type][1], password_xpath)

    # Click button
    def click_on_element(context, xpath):
        context.page.click_element(xpath)

    login_button_xpath = "//button[text()=' Login ']"
    click_on_element(context, login_button_xpath)
