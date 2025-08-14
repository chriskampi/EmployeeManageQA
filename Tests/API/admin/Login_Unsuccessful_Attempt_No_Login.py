import pytest
from data.employees import admin

pytestmark = pytest.mark.api


class TestLoginUnsuccessful:
    """ Test for all unsuccessful login scenarios"""
    ADMIN = admin()

    def test_1_login_wrong_password_response(self):
        """ Test for successful login in case of wrong credentials"""
        self.ADMIN.set_password(1)
        self.ADMIN.login_user_via_api(expected_code=None)
