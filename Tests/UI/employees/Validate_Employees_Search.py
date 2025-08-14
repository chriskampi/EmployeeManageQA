import pytest
from data.employees import qa_tester, new_user, manager_lead_employee, admin

class TestValidateEmployeesSearch:
    """UI tests for validating employee search functionality via the web interface"""

    admin = admin()
    employees = [qa_tester(), new_user(), manager_lead_employee()]

    def test_1_validate_employees_search(self, driver):
        """Test validating employee search functionality via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.employees[0].validate_employees_list(driver, [self.employees[1]], search="New")
        self.employees[0].validate_employees_list(driver, [], search="Wrong")
        self.employees[0].validate_employees_list(driver, self.employees, search="")
