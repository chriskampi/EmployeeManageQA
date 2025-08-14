import pytest
from data.skills import logistics
from data.employees import admin
import time

class TestUpdateSkillViaUI:
    """UI tests for creating skills via the web interface"""

    admin = admin()
    skill = logistics()
    NEW_TITLE = f"Logistic_{time.time()}"
    OLD_TITLE = skill.get_title()
    
    def test_1_create_skill_via_ui(self, driver):
        """Test creating a skill via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.skill.update_skill_via_ui(driver, self.NEW_TITLE)

    def test_2_create_skill_via_ui(self, driver):
        """Test creating a skill via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.skill.update_skill_via_ui(driver, self.OLD_TITLE)