import pytest
from data.skills import create_test_skill

pytestmark = pytest.mark.api

class TestCreateSkillSuccessful:
    
    """ Test for successful skill creation """
    SKILL = create_test_skill()

    def test_create_skill_successful(self):
        """ Test for successful skill creation """
        self.SKILL.create_skill_via_api()

    def test_delete_skill_successful(self):
        """ Test for successful skill deletion """
        self.SKILL.delete_skill_via_api()
