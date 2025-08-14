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

    def login_user_via_api(self, expected_code=200, time=5, content=None):

        url = (f"{self.base_url}/api/admin/login?"
               f"email={self.get_email()}&"
               f"password={self.get_password()}")
        response = requests.get(url, timeout=time)
        assert response.status_code == expected_code
        if expected_code == 200:
            # Convert user_id to string and build the expected content as a string first
            user_id_str = str(self.get_user_id()) if self.get_user_id() else "1"
            firstname_str = self.get_firstname() if self.get_firstname() else "Test"
            lastname_str = self.get_lastname() if self.get_lastname() else "User"
            email_str = self.get_email() if self.get_email() else "test@example.com"
            
            expected_content = (f'{{"success":true,'
                                f'"message":"Login successful",'
                                f'"data":{{'
                                f'"id":{user_id_str},'
                                f'"firstname":"{firstname_str}",'
                                f'"lastname":"{lastname_str}",'
                                f'"email":"{email_str}"'
                                f'}}}}')
            
            # Convert to bytes for comparison with response.content
            expected_content_bytes = expected_content.encode('utf-8')
            assert expected_content_bytes in response.content
        else:
            if content:
                # Convert content to bytes if it's a string
                if isinstance(content, str):
                    content = content.encode('utf-8')
                assert response.content == content

