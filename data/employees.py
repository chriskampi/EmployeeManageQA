from functions.employee import Employee

def qa_tester():

    employee = Employee()
    employee.set_firstname("QA")
    employee.set_lastname("Tester")
    employee.set_email("ckampisios@test.com")

    return employee

def new_user():

    employee = Employee()
    employee.set_firstname("New")
    employee.set_lastname("User")
    employee.set_email("ckamp@test.com")

    return employee

def admin():

    employee = Employee()
    employee.set_firstname("admin")
    employee.set_lastname("admin")
    employee.set_email("admin@test.com")
    employee.set_password("123456")

    return employee