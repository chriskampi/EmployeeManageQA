import pytest
from data.employees import admin, qa_tester

class TestLoginFailedAttempt:
    """UI tests for login failure scenarios"""

    admin = admin()
    admin.set_email(qa_tester().get_email())

    def test_1_login_failed_attempt(self, driver):
        """Test login failure scenario via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login_fail_attempt(driver)