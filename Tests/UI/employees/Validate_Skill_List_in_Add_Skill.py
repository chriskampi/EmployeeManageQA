import pytest
from data.employees import manager_lead_employee, admin
from data.skills import logistics

class TestValidateSkillListInAddSkill:
    """UI tests for creating employees via the web interface"""

    admin = admin()
    employee = manager_lead_employee()
    skills = [logistics()]
    
    def test_1_create_employee_via_ui(self, driver):
        """Test creating an employee via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.employee.validate_skills_in_add(driver, self.skills)
