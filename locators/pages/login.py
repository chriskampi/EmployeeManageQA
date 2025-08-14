from config.selenium_action_utils import SeleniumActions
from conftest import load_config

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = SeleniumActions(driver)
        # Use base_url for UI navigation, not api_base_url
        config = load_config()
        self.url = f"{config.get('base_url', config['api_base_url'])}login"

    __input_email = f"//input[@id='email']"
    __input_password = f"//input[@id='password']"
    __button_login = f"//button[contains(@class,'blue')][contains(.,'Sign in')]"

    def set_text_input_email(self, email):
        """ set email input """
        path = self.__input_email
        self.actions.find_and_type(path, email)

    def set_text_input_password(self, password):
        """ set password input """
        path = self.__input_password
        self.actions.find_and_type(path, password)

    def click_button_login(self):
        """ Click on login button """
        path = self.__button_login
        self.actions.find_and_click(path)

    def validate_div_error(self):
        """ Validate error message div """
        path = "//div[contains(.,'Request failed with status code 500')]"
        self.actions.find(path)