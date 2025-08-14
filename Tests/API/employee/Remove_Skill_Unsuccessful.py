import pytest
from data.employees import qa_tester
from data.skills import management

pytestmark = pytest.mark.api

class TestRemoveSkillUnsuccessful:
    """ Test for all unsuccessful skill removal scenarios"""
    EMPLOYEE = qa_tester()
    SKILL = management()

    def test_1_remove_skill_missing_employee_id_response(self):
        """ Test for unsuccessful skill removal due to missing employee_id"""
        self.EMPLOYEE.set_user_id(None)
        self.EMPLOYEE.remove_skill_via_api(self.SKILL, expected_code=400)

    def test_2_remove_skill_missing_skill_id_response(self):
        """ Test for unsuccessful skill removal due to missing skill_id"""
        self.EMPLOYEE.set_user_id(5)  # Reset employee_id
        self.SKILL.set_id(None)
        self.EMPLOYEE.remove_skill_via_api(self.SKILL, expected_code=400)

    def test_3_remove_skill_invalid_employee_id_response(self):
        """ Test for unsuccessful skill removal due to invalid employee_id"""
        self.SKILL.set_id(4)  # Reset skill_id
        self.EMPLOYEE.set_user_id(999)  # Non-existent employee ID
        self.EMPLOYEE.remove_skill_via_api(self.SKILL, expected_code=404)

    def test_4_remove_skill_invalid_skill_id_response(self):
        """ Test for unsuccessful skill removal due to invalid skill_id"""
        self.EMPLOYEE.set_user_id(5)  # Reset employee_id
        self.SKILL.set_id(999)  # Non-existent skill ID
        self.EMPLOYEE.remove_skill_via_api(self.SKILL, expected_code=404)
