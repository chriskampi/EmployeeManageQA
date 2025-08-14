import pytest
from data.skills import management

pytestmark = pytest.mark.api

class TestUpdateSkillUnsuccessful:
    """ Test for all unsuccessful skill update scenarios"""
    SKILL = management()

    def test_1_update_skill_missing_id_response(self):
        """ Test for unsuccessful skill update due to missing id"""
        self.SKILL.set_id(None)
        skill_data = {
            "title": "Updated Title"
        }
        self.SKILL.update_skill_via_api(skill_data, expected_code=400)

    def test_2_update_skill_missing_title_response(self):
        """ Test for unsuccessful skill update due to missing title in skill_data"""
        self.SKILL.set_id(4)  # Reset id
        skill_data = {
            "title": None
        }
        self.SKILL.update_skill_via_api(skill_data, expected_code=400)

    def test_3_update_skill_empty_title_response(self):
        """ Test for unsuccessful skill update due to empty title in skill_data"""
        skill_data = {
            "title": ""
        }
        self.SKILL.update_skill_via_api(skill_data, expected_code=400)

    def test_4_update_skill_invalid_id_response(self):
        """ Test for unsuccessful skill update due to invalid id"""
        self.SKILL.set_id(999)  # Non-existent ID
        skill_data = {
            "title": "Updated Title"
        }
        self.SKILL.update_skill_via_api(skill_data, expected_code=404)
