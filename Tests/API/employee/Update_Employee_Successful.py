import pytest
from data.employees import qa_tester

pytestmark = pytest.mark.api

class TestUpdateEmployeeSuccessful:
    
    """ Test for successful employee update """
    EMPLOYEE = qa_tester()

    def test_update_employee_successful(self):
        """ Test for successful employee update """
        user_data = {
            "firstname": "Updated",
            "lastname": "QA",
            "email": "updated.qa@test.com"
        }
        self.EMPLOYEE.update_employee_via_api(user_data)
