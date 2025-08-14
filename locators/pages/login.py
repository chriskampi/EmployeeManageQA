from config.selenium_action_utils import SeleniumActions

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = SeleniumActions(driver)

    __input_email = f"//input[@id='email']"
    __input_password = f"//input[@id='password']"
    __button_login = f"//button[contains(@class,'blue')][contains(.,'Sign in')]"

    def set_text_input_email(self, email):
        """ set email input """
        path = self.__input_email
        self.actions.type(path, email)

    def set_text_input_password(self, password):
        """ set password input """
        path = self.__input_password
        self.actions.type(path, password)

    def click_button_login(self):
        """ Click on login button """
        path = self.__button_login
        self.actions.click(path)