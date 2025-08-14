import pytest
from data.employees import qa_tester

pytestmark = pytest.mark.api

class TestGetEmployeesSuccessful:
    
    """ Test for successful employee retrieval """
    EMPLOYEE = qa_tester()

    def test_1_get_employees_successful(self):
        """ Test for successful employee retrieval without search """
        self.EMPLOYEE.get_employees_via_api()

    def test_2_get_employees_search_by_email_successful(self):
        """ Test for successful employee retrieval with email search term """
        self.EMPLOYEE.get_employees_via_api(search="ckampisios@test.com")

    def test_3_get_employees_search_by_firstname_successful(self):
        """ Test for successful employee retrieval with firstname search term """
        self.EMPLOYEE.get_employees_via_api(search="QA")

    def test_4_get_employees_search_by_lastname_successful(self):
        """ Test for successful employee retrieval with lastname search term """
        self.EMPLOYEE.get_employees_via_api(search="Tester")

    def test_5_get_employees_search_by_skill_successful(self):
        """ Test for successful employee retrieval with skill search term """
        self.EMPLOYEE.get_employees_via_api(search="Accountability")

    def test_6_get_employees_search_wrong_term_no_data(self):
        """ Test for successful employee retrieval with wrong search term showing no data """
        self.EMPLOYEE.get_employees_via_api(search="NonExistentTerm")
