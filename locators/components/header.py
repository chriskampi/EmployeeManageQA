from config.selenium_action_utils import SeleniumActions

class Header:
    def __init__(self, driver):
        self.driver = driver
        self.actions = SeleniumActions(driver)

    __header = "//header"
    __button_logout = f"{__header}//button[contains(.,'Logout')]"

    def __path_button_navigate(self, tab):
        """ Navigate to any tab page """

        path = f"{self.__header}//nav/button[contains(.,'{tab}')]"
        return path

    def __path_button_navigate_employee(self):
        """ Navigate to skill page """

        path = f"{self.__path_button_navigate('Employee')}"
        return path

    def __path_button_navigate_skill(self):
        """ Navigate to skill page """
        path = f"{self.__path_button_navigate('Skill')}"
        return path

    def click_button_logout(self):
        """ Click on logout button """
        path = self.__button_logout
        self.actions.click(path)

    def click_button_employee_tab(self):
        """ Click on employee tab """
        path = self.__path_button_navigate_employee()
        self.actions.click(path)

    def click_button_skill_tab(self):
        """ Click on skill tab """
        path = self.__path_button_navigate_skill()
        self.actions.click(path)



