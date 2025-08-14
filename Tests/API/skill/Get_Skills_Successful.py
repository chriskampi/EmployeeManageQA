import pytest
from data.skills import accountability, management, logistics

pytestmark = pytest.mark.api

class TestGetSkillsSuccessful:
    
    """ Test for successful skill retrieval """
    SKILL = accountability()

    def test_1_get_skills_successful(self):
        """ Test for successful skill retrieval without search """
        # Expected all skills - retrieve from data files
        accountability_skill = accountability()
        management_skill = management()
        logistics_skill = logistics()
        
        expected_skills = [
            {
                'id': accountability_skill.get_id(),
                'title': accountability_skill.get_title()
            },
            {
                'id': management_skill.get_id(),
                'title': management_skill.get_title()
            },
            {
                'id': logistics_skill.get_id(),
                'title': logistics_skill.get_title()
            }
        ]
        self.SKILL.get_skills_via_api(expected_skills=expected_skills)

    def test_2_get_skills_search_by_title_successful(self):
        """ Test for successful skill retrieval with title search term """
        # Expected only the skill with matching title
        accountability_skill = accountability()
        expected_skills = [
            {
                'id': accountability_skill.get_id(),
                'title': accountability_skill.get_title()
            }
        ]
        self.SKILL.get_skills_via_api(search=accountability_skill.get_title(), expected_skills=expected_skills)

    def test_3_get_skills_search_by_partial_title_successful(self):
        """ Test for successful skill retrieval with partial title search term """
        # Expected skills with partial title match
        accountability_skill = accountability()
        expected_skills = [
            {
                'id': accountability_skill.get_id(),
                'title': accountability_skill.get_title()
            }
        ]
        self.SKILL.get_skills_via_api(search="Account", expected_skills=expected_skills)

    def test_4_get_skills_search_wrong_term_no_data(self):
        """ Test for successful skill retrieval with wrong search term showing no data """
        # Expected no skills for non-existent search term
        expected_skills = []
        self.SKILL.get_skills_via_api(search="NonExistentSkill", expected_skills=expected_skills)
