class Employee:
    def __init__(self, firstname=None, lastname=None, email=None, password=None):
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._password = password

    # Setters
    def set_firstname(self, firstname):
        self._firstname = firstname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def set_email(self, email):
        self._email = email

    def set_password(self, password):
        self._password = password

    # Getters
    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password
