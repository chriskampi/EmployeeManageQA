from config.selenium_action_utils import SeleniumActions
from time import sleep

class SkillModal:
    def __init__(self, driver):
        self.driver = driver
        self.actions = SeleniumActions(driver)

    __modal_skill = f"//div[@class='mt-3']"
    __select_skill = f"{__modal_skill}//select"

    def __path_option_skill(self, option):
        """ Select skill from dropdown """
        path = f"{self.__select_skill}//option[contains(.,'{option}')]"

        return path

    def path_button_action_skill(self, action):
        """ Click on button to save skill """
        path = f"{self.__modal_skill}//button[contains(.,'{action} Skill')]"
        return path

    def click_option_skill(self, option):
        """ Click on skill from dropdown """
        path_1 = f"{self.__select_skill}"
        self.actions.find_and_click(path_1)
        path_2 = self.__path_option_skill(option)
        self.actions.find_and_click(path_2)

    def click_add_skill(self):
        """ Click on add skill button """
        path = self.path_button_action_skill("Add")
        self.actions.find_and_click(path)
        sleep(1)

    def click_remove_skill(self):
        """ Click on remove skill button """
        path = self.path_button_action_skill("Remove")
        self.actions.find_and_click(path)
        sleep(1)

    def validate_option_skills(self, skills):
        """Validate that the skill dropdown contains the expected skills"""
        # Get all option elements from the select dropdown
        options_xpath = f"{self.__select_skill}//option"
        assert self.actions.validate_list(options_xpath, *skills)
