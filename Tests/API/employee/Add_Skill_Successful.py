import pytest
from data.employees import qa_tester
from data.skills import accountability

pytestmark = pytest.mark.api

class TestAddSkillSuccessful:
    
    """ Test for successful skill addition to employee """
    EMPLOYEE = qa_tester()
    SKILL = accountability()

    def test_add_skill_successful(self):
        """ Test for successful skill addition to employee """
        self.EMPLOYEE.add_skill_via_api(self.SKILL)
