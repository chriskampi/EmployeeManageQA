import pytest
from data.employees import create_UI_employee, admin

class TestCreateEmployeeViaUI:
    """UI tests for creating employees via the web interface"""

    admin = admin()
    employee = create_UI_employee()
    
    def test_1_create_employee_via_ui(self, driver):
        """Test creating an employee via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.employee.create_employee_via_ui(driver)

    def test_2_delete_employee_via_ui(self, driver):
        """Test deleting an employee via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.employee.delete_employee_via_ui(driver)
