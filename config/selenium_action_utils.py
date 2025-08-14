from typing import List
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumActions:
    def __init__(self, driver: WebDriver, wait_seconds: int = 10):
        self.driver = driver
        self.wait_seconds = wait_seconds

    def open_url(self, url: str) -> None:
        """Open a URL in the browser"""
        self.driver.get(url)

    def find(self, xpath: str) -> WebElement:
        """Validate the existence of an xpath and return the element"""
        wait = WebDriverWait(self.driver, self.wait_seconds)
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element

    def find_and_click(self, xpath: str) -> None:
        """After validating the existence of the xpath, click it"""
        element = self.find(xpath)
        element.click()

    def find_and_type(self, xpath: str, text: str) -> None:
        """After validating the existence of the xpath, send keys"""
        element = self.find(xpath)
        element.clear()
        element.send_keys(text)

    def validate_list(self, xpath: str, *expected_items) -> bool:
        """Validate the list of elements in the same xpath and check the count matches"""
        # Find all elements with the xpath
        elements = self.driver.find_elements(By.XPATH, xpath)
        
        # Validate the number of elements matches the expected count
        if len(elements) != len(expected_items):
            return False
        
        # Validate each element contains the expected text
        for element, expected_item in zip(elements, expected_items):
            if expected_item not in element.text:
                return False
        
        return True
