import pytest
from data.employees import new_user

pytestmark = pytest.mark.api

class TestUpdateEmployeeSuccessful:
    
    """ Test for successful employee update """
    EMPLOYEE = new_user()
    OLD_DATA = {"firstname": EMPLOYEE.get_firstname(),
                "lastname": EMPLOYEE.get_lastname(),
                "email": EMPLOYEE.get_email()}

    def test_1update_employee_successful(self):
        """ Test for successful employee update """
        user_data = {
            "firstname": "Updated",
            "lastname": "QA",
            "email": "updated.qa@test.com"
        }
        self.EMPLOYEE.update_employee_via_api(user_data)

    def test_2_revert_employee_successful(self):
        """ Test for successful employee revert """
        self.EMPLOYEE.update_employee_via_api(self.OLD_DATA)
