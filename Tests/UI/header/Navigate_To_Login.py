import pytest
from data.employees import admin

class TestCreateSkillViaUI:
    """UI tests for creating skills via the web interface"""

    admin = admin()

    def test_1_create_skill_via_ui(self, driver):
        """Test creating a skill via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.admin.navigate_to_login(driver)