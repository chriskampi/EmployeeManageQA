import pytest
from data.employees import create_test_employee, qa_tester

pytestmark = pytest.mark.api

class TestCreateEmployeeUnsuccessful:
    """ Test for all unsuccessful employee creation scenarios"""
    EMPLOYEE = create_test_employee()
    EXISTING_EMPLOYEE = qa_tester()

    def test_1_create_employee_missing_firstname_response(self):
        """ Test for unsuccessful employee creation due to missing firstname"""
        self.EMPLOYEE.set_firstname(None)
        self.EMPLOYEE.create_employee_via_api(expected_code=400)

    def test_2_create_employee_missing_lastname_response(self):
        """ Test for unsuccessful employee creation due to missing lastname"""
        self.EMPLOYEE.set_firstname("Test")  # Reset firstname
        self.EMPLOYEE.set_lastname(None)
        self.EMPLOYEE.create_employee_via_api(expected_code=400)

    def test_3_create_employee_missing_email_response(self):
        """ Test for unsuccessful employee creation due to missing email"""
        self.EMPLOYEE.set_lastname("Employee")  # Reset lastname
        self.EMPLOYEE.set_email(None)
        self.EMPLOYEE.create_employee_via_api(expected_code=400)

    def test_3_create_employee_existing_email_response(self):
        """ Test for unsuccessful employee creation due to missing email"""
        self.EMPLOYEE.set_email("ckamp@test.com")  # Reset lastname
        self.EMPLOYEE.set_email(None)
        self.EMPLOYEE.create_employee_via_api(expected_code=400)
