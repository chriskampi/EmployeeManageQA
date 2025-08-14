import pytest
from data.employees import admin

class TestNavigateToLogin:
    """UI tests for navigating to the login page"""

    admin = admin()

    def test_1_navigate_to_login(self, driver):
        """Test navigating to the login page via the UI"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.admin.navigate_to_login(driver)