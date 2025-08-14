from config.selenium_action_utils import SeleniumActions
from conftest import load_config
from locators.components.container import Container

class SkillPage():
    def __init__(self, driver):
        self.driver = driver
        self.actions = SeleniumActions(driver)
        self.url = f"{load_config()['api_base_url']}/skills"
        self.container = Container(self.driver)

    __input_skill_title = f"//input[contains(@placeholder,'Title')]"


    def set_text_input_skill_title(self, skill_title):
        """ set skill title input """
        path = self.__input_skill_title
        self.actions.find_and_type(path, skill_title)
