import requests
import json
import conftest
from conftest import load_config


class Employee:
    def __init__(self, user_id=None, firstname=None, lastname=None, email=None, password=None):
        self._user_id = user_id
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._password = password
        self.base_url = load_config()["api_base_url"]

    # Setters
    def set_user_id(self, user_id):
        self._user_id = user_id

    def set_firstname(self, firstname):
        self._firstname = firstname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def set_email(self, email):
        self._email = email

    def set_password(self, password):
        self._password = password

    # Getters
    def get_user_id(self):
        return self._user_id

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def login_user_via_api(self, expected_code=200, time=1, content=None):

        url = (f"{self.base_url}/api/admin/login?"
               f"email={self.get_email()}&"
               f"password={self.get_password()}")
        response = requests.get(url, timeout=time)
        if not expected_code:
            assert response.status_code != 200
        else:
            assert response.status_code == expected_code
        if expected_code == 200:
            expected_content = (f'{{"success":true,'
                                f'"message":"Login successful",'
                                f'"data":{{'
                                f'"id":{str(self.get_user_id())},'
                                f'"firstname":"{self.get_firstname()}",'
                                f'"lastname":"{self.get_lastname()}",'
                                f'"email":"{self.get_email()}"'
                                f'}}}}')
            
            # Convert to bytes for comparison with response.content
            expected_content_bytes = expected_content.encode('utf-8')
            assert expected_content_bytes in response.content
        if content:
            content = content.encode('utf-8')
            assert response.content == content

