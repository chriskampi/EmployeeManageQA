import requests
import json
import conftest
from conftest import load_config
from functions import pages


class Employee:
    def __init__(self, user_id=None, firstname=None, lastname=None, email=None, password=None):
        """
        Initialize an Employee object with optional user details.
        
        Args:
            user_id: Unique identifier for the employee
            firstname: Employee's first name
            lastname: Employee's last name
            email: Employee's email address
            password: Employee's password for authentication
        """
        self._user_id = user_id
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._password = password
        self.base_url = load_config()["api_base_url"]

    # Setters
    def set_user_id(self, user_id):
        """
        Set the user ID for the employee.
        
        Args:
            user_id: Unique identifier for the employee
        """
        self._user_id = user_id

    def set_firstname(self, firstname):
        """
        Set the first name for the employee.
        
        Args:
            firstname: Employee's first name
        """
        self._firstname = firstname

    def set_lastname(self, lastname):
        """
        Set the last name for the employee.
        
        Args:
            lastname: Employee's last name
        """
        self._lastname = lastname

    def set_email(self, email):
        """
        Set the email address for the employee.
        
        Args:
            email: Employee's email address
        """
        self._email = email

    def set_password(self, password):
        """
        Set the password for the employee.
        
        Args:
            password: Employee's password for authentication
        """
        self._password = password

    # Getters
    def get_user_id(self):
        """
        Get the user ID of the employee.
        
        Returns:
            The unique identifier for the employee
        """
        return self._user_id

    def get_firstname(self):
        """
        Get the first name of the employee.
        
        Returns:
            The employee's first name
        """
        return self._firstname

    def get_lastname(self):
        """
        Get the last name of the employee.
        
        Returns:
            The employee's last name
        """
        return self._lastname

    def get_email(self):
        """
        Get the email address of the employee.
        
        Returns:
            The employee's email address
        """
        return self._email

    def get_password(self):
        """
        Get the password of the employee.
        
        Returns:
            The employee's password for authentication
        """
        return self._password

    def login_user_via_api(self, expected_code=200, time=1, content=None):
        """
        Test the GET /login endpoint for user authentication.
        
        Args:
            expected_code (int): Expected HTTP status code (default: 200)
            time (int): Request timeout in seconds (default: 1)
            content: Expected response content for validation
            
        Returns:
            requests.Response: The API response object
        """
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
            
            expected_content_bytes = expected_content.encode('utf-8')
            assert expected_content_bytes in response.content
        if content:
            content = content.encode('utf-8')
            assert response.content == content

    def get_employees_via_api(self, search=None, expected_code=200, time=1, expected_employees=None):
        """
        Test the GET /getEmployees endpoint
        
        Args:
            search: Optional search term for filtering employees
            expected_code: Expected HTTP status code (default: 200)
            time: Request timeout in seconds (default: 1)
            expected_employees: List of expected employee dictionaries to validate against
        """
        url = f"{self.base_url}/api/employees/getEmployees"
        params = {}
        if search:
            params['search'] = search
            
        response = requests.get(url, params=params, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Employees fetched successfully'
            assert 'data' in response_data
            assert isinstance(response_data['data'], list)
            
            # Validate each employee structure
            for employee in response_data['data']:
                assert 'id' in employee
                assert 'firstname' in employee
                assert 'lastname' in employee
                assert 'email' in employee
                assert 'skills' in employee
                assert isinstance(employee['skills'], list)
                
            # If expected_employees is provided, validate the response matches
            if expected_employees is not None:
                # Build the expected response structure
                expected_response = {
                    "success": True,
                    "message": "Employees fetched successfully",
                    "data": expected_employees
                }
                
                # Assert the response matches the expected structure
                assert response_data == expected_response, \
                    f"Response does not match expected structure. Expected: {expected_response}, Got: {response_data}"
                
        return response

    def create_employee_via_api(self, expected_code=200, time=1):
        """
        Test the POST /createEmployee endpoint
        """
        url = f"{self.base_url}/api/employees/createEmployee"
        payload = {
            "firstname": self.get_firstname(),
            "lastname": self.get_lastname(),
            "email": self.get_email()
        }
        
        response = requests.post(url, json=payload, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Employee created successfully'
            assert 'data' in response_data
            
            data = response_data['data']
            assert 'id' in data
            assert data['firstname'] == self.get_firstname()
            assert data['lastname'] == self.get_lastname()
            assert data['email'] == self.get_email()
            
            self.set_user_id(data['id'])
            
        return response

    def update_employee_via_api(self, user_data, expected_code=200, time=1):
        """
        Test the PUT /updateEmployee endpoint
        """
        url = f"{self.base_url}/api/employees/updateEmployee"
        payload = {
            "id": self.get_user_id(),
            "firstname": user_data.get('firstname'),
            "lastname": user_data.get('lastname'),
            "email": user_data.get('email')
        }
        
        response = requests.put(url, json=payload, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Employee updated successfully'
            assert 'data' in response_data
            
            data = response_data['data']
            assert data['id'] == self.get_user_id()
            assert data['firstname'] == user_data.get('firstname')
            assert data['lastname'] == user_data.get('lastname')
            assert data['email'] == user_data.get('email')
            
            self.set_firstname(user_data.get('firstname'))
            self.set_lastname(user_data.get('lastname'))
            self.set_email(user_data.get('email'))
            
        return response

    def delete_employee_via_api(self, expected_code=200, time=1):
        """
        Test the DELETE /deleteEmployee endpoint
        """
        url = f"{self.base_url}/api/employees/deleteEmployee"
        params = {"id": self.get_user_id()}
        
        response = requests.delete(url, params=params, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Employee deleted successfully'
            
        return response

    def add_skill_via_api(self, skill, expected_code=200, time=1):
        """
        Test the POST /addSkill endpoint
        """
        url = f"{self.base_url}/api/employees/addSkill"
        payload = {
            "employee_id": self.get_user_id(),
            "skill_id": skill.get_id()
        }
        
        response = requests.post(url, json=payload, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Skill added to employee successfully'
            assert 'data' in response_data
            
            data = response_data['data']
            assert data['employee_id'] == self.get_user_id()
            assert data['skill_id'] == skill.get_id()
            
        return response

    def remove_skill_via_api(self, skill, expected_code=200, time=1):
        """
        Test the DELETE /removeSkill endpoint
        """
        url = f"{self.base_url}/api/employees/removeSkill"
        params = {
            "employee_id": self.get_user_id(),
            "skill_id": skill.get_id()
        }
        
        response = requests.delete(url, params=params, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Skill removed from employee successfully'
            
        return response

    def navigate_to_skills_tab(self, driver):
        """Navigate to employees tab and verify URL"""
        skill_page = pages.navigate_to_employees_page(driver)

        skill_page.header.click_button_skill_tab()

        # Get the expected URL from EmployeePage
        from locators.pages.skills import SkillPage
        expected_url = SkillPage(driver).url

        # Assert current URL matches expected URL
        assert driver.current_url == expected_url, f"Expected URL: {expected_url}, Got: {driver.current_url}"

    def navigate_to_login(self, driver):
        """Navigate to employees tab and verify URL"""
        skill_page = pages.navigate_to_employees_page(driver)

        skill_page.header.click_button_logout()

        # Get the expected URL from EmployeePage
        from locators.pages.login import LoginPage
        expected_url = LoginPage(driver).url

        # Assert current URL matches expected URL
        assert driver.current_url == expected_url, f"Expected URL: {expected_url}, Got: {driver.current_url}"

    def login(self, driver):
        """login to the application"""
        login_page = pages.navigate_to_login_page(driver)

        login_page.set_text_input_email(self.get_email())
        login_page.set_text_input_password(self.get_password())
        login_page.click_button_login()

    def login_fail_attempt(self, driver):
        """login to the application"""
        login_page = pages.navigate_to_login_page(driver)

        login_page.set_text_input_email(self.get_email())
        login_page.set_text_input_password(self.get_password())
        login_page.click_button_login()
        login_page.validate_div_error()