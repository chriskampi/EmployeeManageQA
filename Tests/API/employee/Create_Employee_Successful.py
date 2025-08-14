import pytest
from data.employees import create_test_employee

pytestmark = pytest.mark.api

class TestCreateEmployeeSuccessful:
    
    """ Test for successful employee creation """
    EMPLOYEE = create_test_employee()

    def test_create_employee_successful(self):
        """ Test for successful employee creation """
        self.EMPLOYEE.create_employee_via_api()
