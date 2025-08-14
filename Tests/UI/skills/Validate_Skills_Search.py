import pytest
from data.skills import logistics, management, accountability
from data.employees import admin

class TestValidateSkillsSearch:
    """UI tests for creating skills via the web interface"""

    admin = admin()
    skills = [logistics(), management(), accountability()]

    def test_1_create_skill_via_ui(self, driver):
        """Test creating a skill via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.skills[0].validate_skills_list(driver, [self.skills[2]], search="Logistics")
        self.skills[0].validate_skills_list(driver, [self.skills[2]], search="Wrong")
        self.skills[0].validate_skills_list(driver, [self.skills[2]], search="")
