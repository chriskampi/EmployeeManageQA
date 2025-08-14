import pytest
from data.employees import qa_tester
from data.skills import management

pytestmark = pytest.mark.api

class TestRemoveSkillSuccessful:
    
    """ Test for successful skill removal from employee """
    EMPLOYEE = qa_tester()
    SKILL = management()

    def test_remove_skill_successful(self):
        """ Test for successful skill removal from employee """
        self.EMPLOYEE.remove_skill_via_api(self.SKILL)
