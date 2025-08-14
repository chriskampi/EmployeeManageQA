import pytest
from data.employees import new_user

pytestmark = pytest.mark.api

class TestDeleteEmployeeSuccessful:
    
    """ Test for successful employee deletion """
    EMPLOYEE = new_user()

    def test_delete_employee_successful(self):
        """ Test for successful employee deletion """
        self.EMPLOYEE.delete_employee_via_api()
