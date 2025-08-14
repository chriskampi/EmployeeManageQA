import pytest
from data.employees import admin

pytestmark = pytest.mark.api

class TestLoginSuccessful:
    
    """ Test for successful login """
    ADMIN = admin()

    def test_login_successful(self):
        """ Test for successful login """
        self.ADMIN.login_user_via_api()