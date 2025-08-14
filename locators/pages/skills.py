from config.selenium_action_utils import SeleniumActions

class SkillPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = SeleniumActions(driver)

    __input_skill_title = f"//input[contains(@placeholder,'Title')]"


    def set_text_input_skill_title(self, skill_title):
        """ set skill title input """
        path = self.__input_skill_title
        self.actions.type(path, skill_title)
