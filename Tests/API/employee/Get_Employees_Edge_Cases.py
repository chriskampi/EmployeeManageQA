import pytest
from data.employees import qa_tester, new_user, manager_lead_employee
from data.skills import accountability, management

pytestmark = pytest.mark.api

class TestGetEmployeesEdgeCases:
    """ Test for edge cases and different response scenarios in employee retrieval"""
    EMPLOYEE = qa_tester()

    def test_1_get_employees_partial_match_search(self):
        """ Test for employee retrieval with partial search terms"""
        # Test partial firstname match
        new_user_obj = new_user()
        qa_tester_obj = qa_tester()
        manager_obj = manager_lead_employee()
        expected_employees = [
            {
                'email': qa_tester_obj.get_email(),
                'firstname': qa_tester_obj.get_firstname(),
                'id': qa_tester_obj.get_user_id(),
                'lastname': qa_tester_obj.get_lastname(),
                'skills': []
            }
        ]
        self.EMPLOYEE.get_employees_via_api(search="Q", expected_employees=expected_employees)
        
        # Test partial lastname match
        expected_employees = [
            {
                'email': new_user_obj.get_email(),
                'firstname': new_user_obj.get_firstname(),
                'id': new_user_obj.get_user_id(),
                'lastname': new_user_obj.get_lastname(),
                'skills': [{'id': accountability().get_id(), 'title': accountability().get_title()}]
            },
            {
                'email': qa_tester_obj.get_email(),
                'firstname': qa_tester_obj.get_firstname(),
                'id': qa_tester_obj.get_user_id(),
                'lastname': qa_tester_obj.get_lastname(),
                'skills': []
            },
            {
                'email': manager_obj.get_email(),
                'firstname': manager_obj.get_firstname(),
                'id': manager_obj.get_user_id(),
                'lastname': manager_obj.get_lastname(),
                'skills': [{'id': management().get_id(), 'title': management().get_title()},
                           {'id': accountability().get_id(), 'title': accountability().get_title()}]
            }
        ]
        self.EMPLOYEE.get_employees_via_api(search="Test", expected_employees=expected_employees)

    def test_2_get_employees_case_insensitive_search(self):
        """ Test for employee retrieval with case insensitive search"""
        # Test lowercase search
        qa_tester_obj = qa_tester()
        expected_employees = [
            {
                'email': qa_tester_obj.get_email(),
                'firstname': qa_tester_obj.get_firstname(),
                'id': qa_tester_obj.get_user_id(),
                'lastname': qa_tester_obj.get_lastname(),
                'skills': []
            }
        ]
        self.EMPLOYEE.get_employees_via_api(search="qa", expected_employees=expected_employees)
        
        # Test uppercase search
        expected_employees = [
            {
                'email': qa_tester_obj.get_email(),
                'firstname': qa_tester_obj.get_firstname(),
                'id': qa_tester_obj.get_user_id(),
                'lastname': qa_tester_obj.get_lastname(),
                'skills': []
            }
        ]
        self.EMPLOYEE.get_employees_via_api(search="TESTER", expected_employees=expected_employees)

    def test_3_get_employees_numeric_search(self):
        """ Test for employee retrieval with numeric search terms"""
        # Test with numeric search (might search by ID or phone)
        qa_tester_obj = qa_tester()
        expected_employees = []
        self.EMPLOYEE.get_employees_via_api(search=str(qa_tester_obj.get_user_id()), expected_employees=expected_employees)

    def test_4_get_employees_mixed_content_search(self):
        """ Test for employee retrieval with mixed content search"""
        # Test with alphanumeric search
        expected_employees = []
        self.EMPLOYEE.get_employees_via_api(search="QA5", expected_employees=expected_employees)

    def test_5_get_employees_timeout_scenario(self):
        """ Test for employee retrieval with timeout scenario"""
        # Test with very short timeout to simulate slow response
        # Don't validate specific results for timeout test
        self.EMPLOYEE.get_employees_via_api(time=0.1)

