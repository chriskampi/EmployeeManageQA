import time

from config.selenium_action_utils import SeleniumActions


class Container:

    def __init__(self, driver):
        self.driver = driver
        self.actions = SeleniumActions(driver)

    __div_container = f"//div[contains(@class,'screen')]/div[contains(@class,'container')]"
    __button_add_entity = f"//button[contains(@class,'blue')][contains(.,'Add')]"
    __button_edit_entity = f"//button[contains(@class,'blue')][contains(.,'Edit')]"
    __button_delete_entity = f"//button[contains(@class,'red')][contains(.,'Delete')]"
    __input_search = f"//input[contains(@placeholder,'Search')]"
    __tr_entity = f"//tbody/tr"
    __button_save_entity = f"//div[contains(@class,'rounded')]//button[contains(@class,'blue')][@type='submit']"


    def __path_tr_row_entity(self, row):
        """ Path to row entity """
        path = f"{self.__tr_entity}[contains(.,'{row}')]"
        return path

    def click_button_add_entity(self):
        """ Click on add entity button """
        path = self.__button_add_entity
        self.actions.find_and_click(path)

    def click_button_edit_entity(self, row):
        """ Click on edit entity button """
        path = f"{self.__path_tr_row_entity(row)}{self.__button_edit_entity}"
        self.actions.find_and_click(path)

    def click_button_delete_entity(self, row):
        """ Click on delete entity button """
        path = f"{self.__path_tr_row_entity(row)}{self.__button_delete_entity}"
        self.actions.find_and_click(path)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(1)

    def click_button_save_entity(self):
        """ Click on delete entity button """
        path = f"{self.__button_save_entity}"
        self.actions.find_and_click(path)
        time.sleep(1)

    def validate_tr_entity_row_info(self, row, info=None, exists=True):
        """ Validate row entity info """

        path = f"{self.__path_tr_row_entity(row)}[contains(.,'{info}')]"
        assert self.actions.find(path, exists) == exists

    def validate_tr_entity_row_list(self, rows):
        """Validate that the entity row list contains the expected rows"""
        # Use the basic validate_list method
        self.actions.validate_list(f"{self.__path_tr_row_entity('')}", *rows)

    def validate_no_entity_rows(self):
        """Validate that no entity rows are found"""
        return self.actions.validate_no_results(self.__tr_entity)

    def set_text_input_search(self, term):
        """ Path to input search """
        path = self.__input_search
        self.actions.find_and_type(path, term)


