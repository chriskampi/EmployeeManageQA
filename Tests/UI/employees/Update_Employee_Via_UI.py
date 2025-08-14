import pytest
from data.employees import qa_tester, admin
import time

class TestUpdateEmployeeViaUI:
    """UI tests for updating employees via the web interface"""

    admin = admin()
    employee = qa_tester()
    NEW_FIRSTNAME = f"Updated_QA_{time.time()}"
    OLD_FIRSTNAME = employee.get_firstname()
    
    def test_1_update_employee_via_ui(self, driver):
        """Test updating an employee via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.employee.update_employee_via_ui(driver, self.NEW_FIRSTNAME)

    def test_2_restore_employee_via_ui(self, driver):
        """Test restoring employee data via the UI using page objects"""
        # Skip if not in UI mode
        self.admin.login(driver)
        self.employee.update_employee_via_ui(driver, self.OLD_FIRSTNAME)
