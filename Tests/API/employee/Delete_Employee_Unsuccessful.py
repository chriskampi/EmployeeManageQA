import pytest
from data.employees import new_user

pytestmark = pytest.mark.api

class TestDeleteEmployeeUnsuccessful:
    """ Test for all unsuccessful employee deletion scenarios"""
    EMPLOYEE = new_user()

    def test_1_delete_employee_missing_id_response(self):
        """ Test for unsuccessful employee deletion due to missing user_id"""
        self.EMPLOYEE.set_user_id(None)
        self.EMPLOYEE.delete_employee_via_api(expected_code=400)

    def test_2_delete_employee_invalid_id_response(self):
        """ Test for unsuccessful employee deletion due to invalid user_id"""
        self.EMPLOYEE.set_user_id(999)  # Non-existent ID
        self.EMPLOYEE.delete_employee_via_api(expected_code=404)
