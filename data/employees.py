from functions.employee import Employee
from time import time

def qa_tester():
    """
    Create and return a QA tester employee instance.
    
    Returns:
        Employee: A QA tester employee with predefined attributes
    """
    employee = Employee()
    employee.set_user_id(5)
    employee.set_firstname("QA")
    employee.set_lastname("Tester")
    employee.set_email("ckampisios@test.com")

    return employee

def new_user():
    """
    Create and return a new user employee instance.
    
    Returns:
        Employee: A new user employee with predefined attributes
    """
    employee = Employee()
    employee.set_user_id(3)
    employee.set_firstname("New")
    employee.set_lastname("User")
    employee.set_email("ckamp@test.com")

    return employee

def admin():
    """
    Create and return an admin employee instance.
    
    Returns:
        Employee: An admin employee with predefined attributes including password
    """
    employee = Employee()
    employee.set_user_id(1)
    employee.set_firstname("admin")
    employee.set_lastname("admin")
    employee.set_email("admin@test.com")
    employee.set_password("123456")

    return employee

def create_test_employee():
    """
    Create and return a test employee instance with a unique lastname.
    
    Returns:
        Employee: A test employee with unique attributes for testing purposes
    """
    employee = Employee()
    employee.set_firstname("Test")
    employee.set_lastname(f"Employee_{time()}")
    employee.set_email("ckamp.test@test.com")

    return employee

def create_UI_employee():
    """
    Create and return a UI test employee instance with a unique lastname.
    
    Returns:
        Employee: A UI test employee with unique attributes for UI testing
    """
    employee = Employee()
    employee.set_firstname("Test")
    employee.set_lastname(f"UI_{time()}")
    employee.set_email("ckamp2.test@test.com")

    return employee

def manager_lead_employee():
    """
    Create and return a manager lead employee instance.
    
    Returns:
        Employee: A manager lead employee with predefined attributes
    """
    employee = Employee()
    employee.set_user_id(9)
    employee.set_firstname("Manager")
    employee.set_lastname("Lead")
    employee.set_email("manager@test.com")

    return employee