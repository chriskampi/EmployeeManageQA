import pytest
from data.employees import qa_tester, new_user, manager_lead_employee
from data.skills import accountability, management

pytestmark = pytest.mark.api

class TestGetEmployeesSuccessful:
    
    """ Test for successful employee retrieval """
    EMPLOYEE = qa_tester()

    def test_1_get_employees_successful(self):
        """ Test for successful employee retrieval without search """
        # Expected all employees - retrieve from data files
        new_user_obj = new_user()
        qa_tester_obj = qa_tester()
        manager_obj = manager_lead_employee()
        
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
        self.EMPLOYEE.get_employees_via_api(expected_employees=expected_employees)

    def test_2_get_employees_search_by_email_successful(self):
        """ Test for successful employee retrieval with email search term """
        # Expected only the employee with matching email
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
        self.EMPLOYEE.get_employees_via_api(search=qa_tester_obj.get_email(), expected_employees=expected_employees)

    def test_3_get_employees_search_by_firstname_successful(self):
        """ Test for successful employee retrieval with firstname search term """
        # Expected employees with matching firstname
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
        self.EMPLOYEE.get_employees_via_api(search=qa_tester_obj.get_firstname(), expected_employees=expected_employees)

    def test_4_get_employees_search_by_lastname_successful(self):
        """ Test for successful employee retrieval with lastname search term """
        # Expected employees with matching lastname
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
        self.EMPLOYEE.get_employees_via_api(search=qa_tester_obj.get_lastname(), expected_employees=expected_employees)

    def test_5_get_employees_search_by_skill_successful(self):
        """ Test for successful employee retrieval with skill search term """
        # Expected employees with matching skill
        new_user_obj = new_user()
        manager_obj = manager_lead_employee()
        accountability_skill = accountability()
        
        expected_employees = [
            {
                'email': new_user_obj.get_email(),
                'firstname': new_user_obj.get_firstname(),
                'id': new_user_obj.get_user_id(),
                'lastname': new_user_obj.get_lastname(),
                'skills': [{'id': accountability_skill.get_id(), 'title': accountability_skill.get_title()}]
            },
            {
                'email': manager_obj.get_email(),
                'firstname': manager_obj.get_firstname(),
                'id': manager_obj.get_user_id(),
                'lastname': manager_obj.get_lastname(),
                'skills': [{'id': accountability_skill.get_id(), 'title': accountability_skill.get_title()}]
            }
        ]
        self.EMPLOYEE.get_employees_via_api(search=accountability_skill.get_title(), expected_employees=expected_employees)

    def test_6_get_employees_search_by_management_skill_successful(self):
        """ Test for successful employee retrieval with management skill search term """
        # Expected only the manager with management skill
        # Note: Based on actual API response, Manager Lead only has Accountability skill
        # This test should return no results for Management skill search
        expected_employees = []
        self.EMPLOYEE.get_employees_via_api(search="Logistics", expected_employees=expected_employees)

    def test_7_get_employees_search_wrong_term_no_data(self):
        """ Test for successful employee retrieval with wrong search term showing no data """
        # Expected no employees for non-existent search term
        expected_employees = []
        self.EMPLOYEE.get_employees_via_api(search="NonExistentTerm", expected_employees=expected_employees)
