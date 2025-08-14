import pytest
from data.skills import create_test_skill, accountability

pytestmark = pytest.mark.api

class TestCreateSkillUnsuccessful:
    """ Test for all unsuccessful skill creation scenarios"""
    SKILL = create_test_skill()
    EXISTING_SKILL = accountability()

    def test_1_create_skill_missing_title_response(self):
        """ Test for unsuccessful skill creation due to missing title"""
        self.SKILL.set_title(None)
        self.SKILL.create_skill_via_api(expected_code=400)

    def test_2_create_skill_empty_title_response(self):
        """ Test for unsuccessful skill creation due to empty title"""
        self.SKILL.set_title("")
        self.SKILL.create_skill_via_api(expected_code=400)

    def test_3_create_skill_existing_title_response(self):
        """ Test for unsuccessful skill creation due to existing title"""
        self.SKILL.set_title(self.EXISTING_SKILL.get_title())
        self.SKILL.create_skill_via_api(expected_code=400)
