import pytest
from data.employees import qa_tester
from data.skills import accountability

pytestmark = pytest.mark.api

class TestAddSkillUnsuccessful:
    """ Test for all unsuccessful skill addition scenarios"""
    EMPLOYEE = qa_tester()
    SKILL = accountability()

    def test_1_add_skill_missing_employee_id_response(self):
        """ Test for unsuccessful skill addition due to missing employee_id"""
        self.EMPLOYEE.set_user_id(None)
        self.EMPLOYEE.add_skill_via_api(self.SKILL, expected_code=400)

    def test_2_add_skill_missing_skill_id_response(self):
        """ Test for unsuccessful skill addition due to missing skill_id"""
        self.EMPLOYEE.set_user_id(5)  # Reset employee_id
        self.SKILL.set_id(None)
        self.EMPLOYEE.add_skill_via_api(self.SKILL, expected_code=400)

    def test_3_add_skill_invalid_employee_id_response(self):
        """ Test for unsuccessful skill addition due to invalid employee_id"""
        self.SKILL.set_id(5)  # Reset skill_id
        self.EMPLOYEE.set_user_id(999)  # Non-existent employee ID
        self.EMPLOYEE.add_skill_via_api(self.SKILL, expected_code=404)

    def test_4_add_skill_invalid_skill_id_response(self):
        """ Test for unsuccessful skill addition due to invalid skill_id"""
        self.EMPLOYEE.set_user_id(5)  # Reset employee_id
        self.SKILL.set_id(999)  # Non-existent skill ID
        self.EMPLOYEE.add_skill_via_api(self.SKILL, expected_code=404)
