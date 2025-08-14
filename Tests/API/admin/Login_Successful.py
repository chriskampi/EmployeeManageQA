import pytest
from data.employees import admin

pytestmark = pytest.mark.api

class TestLoginSuccessful:

    def test_login_successful(self):
        admin().login_user_via_api()