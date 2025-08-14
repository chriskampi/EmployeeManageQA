import pytest
from data.skills import accountability

pytestmark = pytest.mark.api

class TestGetSkillsUnsuccessful:
    """ Test for all unsuccessful skill retrieval scenarios"""
    SKILL = accountability()

    def test_1_get_skills_invalid_search_format_response(self):
        """ Test for unsuccessful skill retrieval due to invalid search format"""
        # Test with very long search term that might exceed API limits
        long_search = "a" * 1000
        self.SKILL.get_skills_via_api(search=long_search, expected_code=400)

    def test_2_get_skills_special_characters_search_response(self):
        """ Test for unsuccessful skill retrieval due to special characters in search"""
        # Test with special characters that might cause issues
        special_search = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        self.SKILL.get_skills_via_api(search=special_search, expected_code=400)

    def test_3_get_skills_sql_injection_search_response(self):
        """ Test for unsuccessful skill retrieval due to SQL injection attempt"""
        # Test with potential SQL injection
        sql_injection = "'; DROP TABLE skills; --"
        self.SKILL.get_skills_via_api(search=sql_injection, expected_code=400)

    def test_4_get_skills_empty_search_response(self):
        """ Test for unsuccessful skill retrieval due to empty search string"""
        # Test with empty search string
        self.SKILL.get_skills_via_api(search="", expected_code=400)

    def test_5_get_skills_whitespace_only_search_response(self):
        """ Test for unsuccessful skill retrieval due to whitespace only search"""
        # Test with whitespace only
        self.SKILL.get_skills_via_api(search="   ", expected_code=400)
