import pytest
from data.skills import create_test_skill_UI
from data.employees import admin

class TestCreateSkillViaUI:
    """UI tests for creating skills via the web interface"""

    admin = admin()
    skill = create_test_skill_UI()
    
    def test_1_create_skill_via_ui(self, driver):
        """Test creating a skill via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.skill.create_skill_via_ui(driver)

    def test_2_create_skill_via_ui(self, driver):
        """Test creating a skill via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.skill.delete_skill_via_ui(driver)