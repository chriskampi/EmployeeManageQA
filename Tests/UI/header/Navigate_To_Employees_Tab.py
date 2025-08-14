import pytest
from functions.skill import Skill
from data.employees import admin

class TestNavigateToEmployeesTab:
    """UI tests for navigating to the employees tab"""

    admin = admin()
    skill = Skill()
    
    def test_1_navigate_to_employees_tab(self, driver):
        """Test navigating to the employees tab via the UI"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.skill.navigate_to_employees_tab(driver)