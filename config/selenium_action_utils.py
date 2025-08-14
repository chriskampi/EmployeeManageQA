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

    def find(self, xpath: str, exists: bool = True) -> WebElement | bool:
        """
        Validate the existence of an xpath and optionally return the element
        
        Args:
            xpath: The XPath to find
            exists: If True, return the element. If False, just validate existence and return True/False
            
        Returns:
            WebElement if exists=True, bool if exists=False
        """
        if exists:
            # Original behavior - wait for element and return it
            wait = WebDriverWait(self.driver, self.wait_seconds)
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            return element
        else:
            # Just check if element exists without waiting
            try:
                wait = WebDriverWait(self.driver, 0)  # No wait
                element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                return True
            except:
                return False

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
        """
        Validate the list of elements in the same xpath and check the count matches
        
        Args:
            xpath: The XPath to find elements
            *expected_items: Variable number of expected text items to find
            
        Returns:
            bool: True if all expected items are found, False otherwise
        """
        # Find all elements with the xpath
        elements = self.driver.find_elements(By.XPATH, xpath)
        
        # Validate the number of elements matches the expected count
        if len(elements) != len(expected_items):
            return False
        
        # Validate each element contains the expected text
        for element, expected_item in zip(elements, expected_items):
            # Convert expected_item to string for comparison
            if str(expected_item) not in element.text:
                return False
        
        return True

    def validate_no_results(self, xpath: str) -> bool:
        """
        Validate that no elements are found for the given xpath
        
        Args:
            xpath: The XPath to check
            
        Returns:
            bool: True if no elements found, False if elements exist
        """
        elements = self.driver.find_elements(By.XPATH, xpath)
        return len(elements) == 0
