import pytest
from data.employees import qa_tester

pytestmark = pytest.mark.api

class TestUpdateEmployeeUnsuccessful:
    """ Test for all unsuccessful employee update scenarios"""
    EMPLOYEE = qa_tester()

    def test_1_update_employee_missing_id_response(self):
        """ Test for unsuccessful employee update due to missing user_id"""
        self.EMPLOYEE.set_user_id(None)
        user_data = {
            "firstname": "Updated",
            "lastname": "QA",
            "email": "updated.qa@test.com"
        }
        self.EMPLOYEE.update_employee_via_api(user_data, expected_code=400)

    def test_2_update_employee_missing_firstname_response(self):
        """ Test for unsuccessful employee update due to missing firstname in user_data"""
        self.EMPLOYEE.set_user_id(5)  # Reset user_id
        user_data = {
            "firstname": None,
            "lastname": "QA",
            "email": "updated.qa@test.com"
        }
        self.EMPLOYEE.update_employee_via_api(user_data, expected_code=400)

    def test_3_update_employee_missing_lastname_response(self):
        """ Test for unsuccessful employee update due to missing lastname in user_data"""
        user_data = {
            "firstname": "Updated",
            "lastname": None,
            "email": "updated.qa@test.com"
        }
        self.EMPLOYEE.update_employee_via_api(user_data, expected_code=400)

    def test_4_update_employee_missing_email_response(self):
        """ Test for unsuccessful employee update due to missing email in user_data"""
        user_data = {
            "firstname": "Updated",
            "lastname": "QA",
            "email": None
        }
        self.EMPLOYEE.update_employee_via_api(user_data, expected_code=400)
