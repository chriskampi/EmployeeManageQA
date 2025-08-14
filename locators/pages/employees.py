from config.selenium_action_utils import SeleniumActions
from conftest import load_config
from locators.components.employee_skill_modal import skillModal
from locators.components.container import Container
from locators.components.header import Header

class EmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = SeleniumActions(driver)
        # Use base_url for UI navigation, not api_base_url
        config = load_config()
        self.url = f"{config.get('base_url', config['api_base_url'])}employees"
        self.container = Container(self.driver)
        self.skill_modal = skillModal(self.driver)
        self.header = Header(self.driver)

    __button_add_skill = f"//button[contains(@class,'green')][contains(.,'Add Skill')]"
    __button_delete_skill = f"//button[contains(@class,'orange')][contains(.,'Remove Skill')]"
    __input_firstname = f"//input[contains(@placeholder,'First Name')]"
    __input_lastname = f"//input[contains(@placeholder,'Last Name')]"
    __input_email = f"//input[contains(@placeholder,'Email')]"

    def click_button_add_skill(self):
        """ Click on add skill button """
        path = self.__button_add_skill
        self.actions.find_and_click(path)

    def click_button_delete_skill(self):
        """ Click on remove skill button """
        path = self.__button_delete_skill
        self.actions.find_and_click(path)

    def set_text_input_firstname(self, firstname):
        """ set firstname input """
        path = self.__input_firstname
        self.actions.find_and_type(path, firstname)

    def set_text_input_lastname(self, lastname):
        """ set lastname input """
        path = self.__input_lastname
        self.actions.find_and_type(path, lastname)

    def set_text_input_email(self, email):
        """ set email input """
        path = self.__input_email
        self.actions.find_and_type(path, email)
    

