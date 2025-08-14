import pytest
from data.employees import qa_tester, admin
from data.skills import logistics

class TestManageEmployeeSkillsViaUI:
    """UI tests for managing employee skills via the web interface"""

    admin = admin()
    employee = qa_tester()
    skill = logistics()
    
    def test_1_add_skill_to_employee_via_ui(self, driver):
        """Test adding a skill to an employee via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.employee.add_skill_to_employee_via_ui(driver, self.skill)

    def test_2_remove_skill_from_employee_via_ui(self, driver):
        """Test removing a skill from an employee via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.employee.remove_skill_from_employee_via_ui(driver, self.skill)
