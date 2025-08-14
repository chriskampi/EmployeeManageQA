import pytest
from functions.skill import Skill
from data.employees import admin

class TestCreateSkillViaUI:
    """UI tests for creating skills via the web interface"""

    admin = admin()
    skill = Skill()
    
    def test_1_create_skill_via_ui(self, driver):
        """Test creating a skill via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.skill.navigate_to_employees_tab(driver)