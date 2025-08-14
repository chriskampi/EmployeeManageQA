import pytest
from data.skills import management

pytestmark = pytest.mark.api

class TestUpdateSkillSuccessful:
    
    """ Test for successful skill update """
    SKILL = management()
    OLD_DATA = {"title": SKILL.get_title()}

    def test_1_update_skill_successful(self):
        """ Test for successful skill update """
        skill_data = {
            "title": "Updated Management"
        }
        self.SKILL.update_skill_via_api(skill_data)

    def test_2_revert_skill_successful(self):
        """ Test for successful skill revert """
        self.SKILL.update_skill_via_api(self.OLD_DATA)
