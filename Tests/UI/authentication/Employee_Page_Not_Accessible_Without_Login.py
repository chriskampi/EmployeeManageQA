import pytest
from functions.pages import navigate_to_employees_page
from locators.pages.login import LoginPage

class TestEmployeePageNotAccessibleWithoutLogin:
    """Validate employee page is not accessible without login"""


    def test_1_add_skill_to_employee_via_ui(self, driver):
        """ Test getting the hard url"""
        # Skip if not in UI mode
        navigate_to_employees_page(driver)
        expected_url = LoginPage(driver).url
        assert driver.current_url == expected_url, "Page should not be accessible without login"

