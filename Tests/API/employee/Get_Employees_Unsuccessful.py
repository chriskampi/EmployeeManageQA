import pytest
from data.employees import qa_tester

pytestmark = pytest.mark.api

class TestGetEmployeesUnsuccessful:
    """ Test for all unsuccessful employee retrieval scenarios"""
    EMPLOYEE = qa_tester()

    def test_1_get_employees_invalid_search_format_response(self):
        """ Test for unsuccessful employee retrieval due to invalid search format"""
        # Test with very long search term that might exceed API limits
        long_search = "a" * 1000
        self.EMPLOYEE.get_employees_via_api(search=long_search, expected_code=400)

    def test_2_get_employees_special_characters_search_response(self):
        """ Test for unsuccessful employee retrieval due to special characters in search"""
        # Test with special characters that might cause issues
        special_search = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        self.EMPLOYEE.get_employees_via_api(search=special_search, expected_code=400)

    def test_3_get_employees_sql_injection_search_response(self):
        """ Test for unsuccessful employee retrieval due to SQL injection attempt"""
        # Test with potential SQL injection
        sql_injection = "'; DROP TABLE employees; --"
        self.EMPLOYEE.get_employees_via_api(search=sql_injection, expected_code=400)

    def test_4_get_employees_empty_search_response(self):
        """ Test for unsuccessful employee retrieval due to empty search string"""
        # Test with empty search string
        self.EMPLOYEE.get_employees_via_api(search="", expected_code=400)

    def test_5_get_employees_whitespace_only_search_response(self):
        """ Test for unsuccessful employee retrieval due to whitespace only search"""
        # Test with whitespace only
        self.EMPLOYEE.get_employees_via_api(search="   ", expected_code=400)
