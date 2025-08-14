from functions.employee import Employee

def qa_tester():

    employee = Employee()
    employee.set_user_id(5)
    employee.set_firstname("QA")
    employee.set_lastname("Tester")
    employee.set_email("ckampisios@test.com")

    return employee

def new_user():

    employee = Employee()
    employee.set_user_id(3)
    employee.set_firstname("New")
    employee.set_lastname("User")
    employee.set_email("ckamp@test.com")

    return employee

def admin():

    employee = Employee()
    employee.set_user_id(1)
    employee.set_firstname("admin")
    employee.set_lastname("admin")
    employee.set_email("admin@test.com")
    employee.set_password("123456")

    return employee

def create_test_employee():

    employee = Employee()
    employee.set_firstname("Test")
    employee.set_lastname("Employee")
    employee.set_email("ckamp.test@test.com")

    return employee

def manager_lead_employee():

    employee = Employee()
    employee.set_firstname("Test")
    employee.set_lastname("Employee")
    employee.set_email("ckamp.test@test.com")

    return employee