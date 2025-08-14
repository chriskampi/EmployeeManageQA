import pytest
from data.employees import qa_tester

pytestmark = pytest.mark.api

class TestGetEmployeesEdgeCases:
    """ Test for edge cases and different response scenarios in employee retrieval"""
    EMPLOYEE = qa_tester()

    def test_1_get_employees_partial_match_search(self):
        """ Test for employee retrieval with partial search terms"""
        # Test partial firstname match
        self.EMPLOYEE.get_employees_via_api(search="Q")
        
        # Test partial lastname match
        self.EMPLOYEE.get_employees_via_api(search="Test")

    def test_2_get_employees_case_insensitive_search(self):
        """ Test for employee retrieval with case insensitive search"""
        # Test lowercase search
        self.EMPLOYEE.get_employees_via_api(search="qa")
        
        # Test uppercase search
        self.EMPLOYEE.get_employees_via_api(search="TESTER")

    def test_3_get_employees_numeric_search(self):
        """ Test for employee retrieval with numeric search terms"""
        # Test with numeric search (might search by ID or phone)
        self.EMPLOYEE.get_employees_via_api(search="5")

    def test_4_get_employees_mixed_content_search(self):
        """ Test for employee retrieval with mixed content search"""
        # Test with alphanumeric search
        self.EMPLOYEE.get_employees_via_api(search="QA5")

    def test_5_get_employees_timeout_scenario(self):
        """ Test for employee retrieval with timeout scenario"""
        # Test with very short timeout to simulate slow response
        self.EMPLOYEE.get_employees_via_api(time=0.1)

    def test_6_get_employees_large_dataset_response(self):
        """ Test for employee retrieval with large dataset response"""
        # Test without search to get all employees (large dataset)
        self.EMPLOYEE.get_employees_via_api()
        
        # Verify response structure for large datasets
        response = self.EMPLOYEE.get_employees_via_api()
        assert response.status_code == 200
        response_data = response.json()
        assert 'data' in response_data
        assert isinstance(response_data['data'], list)
