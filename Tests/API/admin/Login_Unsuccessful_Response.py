import pytest
from data.employees import admin

pytestmark = pytest.mark.api


class TestLoginUnsuccessful:
    """ Test for all unsuccessful login scenarios"""
    ADMIN = admin()

    def test_1_login_wrong_password_response(self):
        """ Test for successful login in case of wrong password"""
        self.ADMIN.set_password(1)
        self.ADMIN.login_user_via_api(expected_code=401, content= "Invalid email or password")

    def test_2_login_wrong_email_response(self):
        """ Test for successful login in case of wrong email"""
        self.ADMIN.set_email(1)
        self.ADMIN.login_user_via_api(expected_code=401, content= "Invalid email or password")