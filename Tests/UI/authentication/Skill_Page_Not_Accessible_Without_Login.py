import pytest
from functions.pages import navigate_to_skills_page
from locators.pages.login import LoginPage

class TestEmployeePageNotAccessibleWithoutLogin:
    """Validate skill page is not accessible without login"""


    def test_1_get_hard_url(self, driver):
        """ Test getting the hard url"""
        navigate_to_skills_page(driver)
        expected_url = LoginPage(driver).url
        assert driver.current_url == expected_url, "Page should not be accessible without login"

