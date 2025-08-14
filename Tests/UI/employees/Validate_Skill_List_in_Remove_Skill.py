import pytest
from data.employees import manager_lead_employee, admin
from data.skills import management, accountability

class TestValidateSkillListInRemoveSkill:
    """UI tests for validating skill list in remove skill functionality"""

    admin = admin()
    employee = manager_lead_employee()
    skills = [accountability(), management()]
    
    def test_1_validate_skill_list_in_remove_skill(self, driver):
        """Test validating the skill list in remove skill functionality"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.employee.validate_skills_in_remove(driver, self.skills)
