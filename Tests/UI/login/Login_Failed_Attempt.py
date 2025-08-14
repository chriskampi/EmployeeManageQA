import pytest
from data.employees import admin, qa_tester

class TestCreateSkillViaUI:
    """UI tests for creating skills via the web interface"""

    admin = admin()
    admin.set_email(qa_tester().get_email())

    def test_1_create_skill_via_ui(self, driver):
        """Test creating a skill via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login_fail_attempt(driver)