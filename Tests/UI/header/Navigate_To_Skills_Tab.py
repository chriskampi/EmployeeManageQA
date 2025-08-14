import pytest
from data.employees import admin

class TestNavigateToSkillsTab:
    """UI tests for navigating to the skills tab"""

    admin = admin()

    def test_1_navigate_to_skills_tab(self, driver):
        """Test navigating to the skills tab via the UI"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.admin.navigate_to_skills_tab(driver)