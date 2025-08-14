import pytest
from data.skills import logistics

pytestmark = pytest.mark.api

class TestDeleteSkillSuccessful:
    
    """ Test for successful skill deletion """
    SKILL = logistics()

    def test_delete_skill_successful(self):
        """ Test for successful skill deletion """
        self.SKILL.delete_skill_via_api()
