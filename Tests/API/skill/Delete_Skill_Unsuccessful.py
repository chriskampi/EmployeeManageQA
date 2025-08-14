import pytest
from data.skills import logistics

pytestmark = pytest.mark.api

class TestDeleteSkillUnsuccessful:
    """ Test for all unsuccessful skill deletion scenarios"""
    SKILL = logistics()

    def test_1_delete_skill_missing_id_response(self):
        """ Test for unsuccessful skill deletion due to missing id"""
        self.SKILL.set_id(None)
        self.SKILL.delete_skill_via_api(expected_code=400)

    def test_2_delete_skill_invalid_id_response(self):
        """ Test for unsuccessful skill deletion due to invalid id"""
        self.SKILL.set_id(999)  # Non-existent ID
        self.SKILL.delete_skill_via_api(expected_code=404)
