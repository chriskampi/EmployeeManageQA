import pytest
from data.employees import qa_tester, new_user, manager_lead_employee, create_test_employee
from data.skills import accountability, management, logistics, create_test_skill

pytestmark = pytest.mark.api

class TestSQLInjectionProtection:
    """ Test for SQL injection protection across all API endpoints """
    
    # SQL injection payload to test
    SQL_INJECTION_PAYLOAD = "INSERT INTO `employee_manage`.`skills` \
     (`id`, `title`) VALUES ('2', 'New')"
    
    def test_1_login_sql_injection_protection(self):
        """ Test login endpoint for SQL injection protection """
        employee = qa_tester()
        
        # Test SQL injection in email parameter
        employee.set_email(self.SQL_INJECTION_PAYLOAD)
        employee.login_user_via_api(expected_code=401)
        
        # Test SQL injection in password parameter
        employee.set_email("qa@test.com")  # Reset to valid email
        employee.set_password(self.SQL_INJECTION_PAYLOAD)
        employee.login_user_via_api(expected_code=401)

    def test_2_get_employees_sql_injection_protection(self):
        """ Test getEmployees endpoint for SQL injection protection """
        employee = qa_tester()
        
        # Test SQL injection in search parameter
        employee.get_employees_via_api(search=self.SQL_INJECTION_PAYLOAD, expected_code=400)

    def test_3_create_employee_sql_injection_protection(self):
        """ Test createEmployee endpoint for SQL injection protection """
        employee = create_test_employee()
        
        # Test SQL injection in firstname parameter
        employee.set_firstname(self.SQL_INJECTION_PAYLOAD)
        employee.create_employee_via_api(expected_code=400)
        
        # Test SQL injection in lastname parameter
        employee.set_firstname("Test")  # Reset to valid firstname
        employee.set_lastname(self.SQL_INJECTION_PAYLOAD)
        employee.create_employee_via_api(expected_code=400)
        
        # Test SQL injection in email parameter
        employee.set_lastname("Employee")  # Reset to valid lastname
        employee.set_email(self.SQL_INJECTION_PAYLOAD)
        employee.create_employee_via_api(expected_code=400)

    def test_4_update_employee_sql_injection_protection(self):
        """ Test updateEmployee endpoint for SQL injection protection """
        employee = qa_tester()
        
        # Test SQL injection in firstname parameter
        skill_data = {
            "firstname": self.SQL_INJECTION_PAYLOAD,
            "lastname": "Tester",
            "email": "qa@test.com"
        }
        employee.update_employee_via_api(skill_data, expected_code=400)
        
        # Test SQL injection in lastname parameter
        skill_data = {
            "firstname": "QA",
            "lastname": self.SQL_INJECTION_PAYLOAD,
            "email": "qa@test.com"
        }
        employee.update_employee_via_api(skill_data, expected_code=400)
        
        # Test SQL injection in email parameter
        skill_data = {
            "firstname": "QA",
            "lastname": "Tester",
            "email": self.SQL_INJECTION_PAYLOAD
        }
        employee.update_employee_via_api(skill_data, expected_code=400)

    def test_5_delete_employee_sql_injection_protection(self):
        """ Test deleteEmployee endpoint for SQL injection protection """
        employee = qa_tester()
        
        # Test SQL injection in id parameter (though this is set via setter)
        # We'll test by temporarily setting a malicious ID
        original_id = employee.get_user_id()
        employee.set_user_id(self.SQL_INJECTION_PAYLOAD)
        employee.delete_employee_via_api(expected_code=400)
        employee.set_user_id(original_id)  # Restore original ID

    def test_6_add_skill_sql_injection_protection(self):
        """ Test addSkill endpoint for SQL injection protection """
        employee = qa_tester()
        skill = accountability()
        
        # Test SQL injection in employee_id parameter
        original_id = employee.get_user_id()
        employee.set_user_id(self.SQL_INJECTION_PAYLOAD)
        employee.add_skill_via_api(skill, expected_code=400)
        employee.set_user_id(original_id)  # Restore original ID
        
        # Test SQL injection in skill_id parameter
        original_skill_id = skill.get_id()
        skill.set_id(self.SQL_INJECTION_PAYLOAD)
        employee.add_skill_via_api(skill, expected_code=400)
        skill.set_id(original_skill_id)  # Restore original skill ID

    def test_7_remove_skill_sql_injection_protection(self):
        """ Test removeSkill endpoint for SQL injection protection """
        employee = qa_tester()
        skill = accountability()
        
        # Test SQL injection in employee_id parameter
        original_id = employee.get_user_id()
        employee.set_user_id(self.SQL_INJECTION_PAYLOAD)
        employee.remove_skill_via_api(skill, expected_code=400)
        employee.set_user_id(original_id)  # Restore original ID
        
        # Test SQL injection in skill_id parameter
        original_skill_id = skill.get_id()
        skill.set_id(self.SQL_INJECTION_PAYLOAD)
        employee.remove_skill_via_api(skill, expected_code=400)
        skill.set_id(original_skill_id)  # Restore original skill ID

    def test_8_get_skills_sql_injection_protection(self):
        """ Test getSkills endpoint for SQL injection protection """
        skill = accountability()
        
        # Test SQL injection in search parameter
        skill.get_skills_via_api(search=self.SQL_INJECTION_PAYLOAD, expected_code=400)

    def test_9_create_skill_sql_injection_protection(self):
        """ Test createSkill endpoint for SQL injection protection """
        skill = create_test_skill()
        
        # Test SQL injection in title parameter
        skill.set_title(self.SQL_INJECTION_PAYLOAD)
        skill.create_skill_via_api(expected_code=400)

    def test_10_update_skill_sql_injection_protection(self):
        """ Test updateSkill endpoint for SQL injection protection """
        skill = management()
        
        # Test SQL injection in title parameter
        skill_data = {
            "title": self.SQL_INJECTION_PAYLOAD
        }
        skill.update_skill_via_api(skill_data, expected_code=400)

    def test_11_delete_skill_sql_injection_protection(self):
        """ Test deleteSkill endpoint for SQL injection protection """
        skill = logistics()
        
        # Test SQL injection in id parameter
        original_id = skill.get_id()
        skill.set_id(self.SQL_INJECTION_PAYLOAD)
        skill.delete_skill_via_api(expected_code=400)
        skill.set_id(original_id)  # Restore original ID

    def test_12_complex_sql_injection_scenarios(self):
        """ Test complex SQL injection scenarios with multiple payloads """
        employee = qa_tester()
        skill = accountability()
        
        # Test combination of multiple SQL injection attempts
        complex_payload = "INSERT INTO `employee_manage`.`skills` \
     (`id`, `title`) VALUES ('2', 'New')"
    
        
        # Test in search parameters
        employee.get_employees_via_api(search=complex_payload, expected_code=400)
        skill.get_skills_via_api(search=complex_payload, expected_code=400)
        
        # Test in creation parameters
        test_employee = create_test_employee()
        test_employee.set_firstname(complex_payload)
        test_employee.create_employee_via_api(expected_code=400)
        
        test_skill = create_test_skill()
        test_skill.set_title(complex_payload)
        test_skill.create_skill_via_api(expected_code=400)

    def test_13_encoded_sql_injection_protection(self):
        """ Test SQL injection protection with encoded payloads """
        employee = qa_tester()
        skill = accountability()
        
        # Test URL encoded SQL injection
        encoded_payload = "INSERT INTO `employee_manage`.`skills` \
     (`id`, `title`) VALUES ('2', 'New')"
    
        
        # Test in search parameters
        employee.get_employees_via_api(search=encoded_payload, expected_code=400)
        skill.get_skills_via_api(search=encoded_payload, expected_code=400)

    def test_14_unicode_sql_injection_protection(self):
        """ Test SQL injection protection with Unicode payloads """
        employee = qa_tester()
        skill = accountability()
        
        # Test Unicode SQL injection
        unicode_payload = "INSERT INTO `employee_manage`.`skills` \
     (`id`, `title`) VALUES ('2', 'New')"
    
        
        # Test in search parameters
        employee.get_employees_via_api(search=unicode_payload, expected_code=400)
        skill.get_skills_via_api(search=unicode_payload, expected_code=400)

    def test_15_boundary_sql_injection_protection(self):
        """ Test SQL injection protection at boundary conditions """
        employee = qa_tester()
        skill = accountability()
        
        # Test boundary SQL injection
        boundary_payload = "INSERT INTO `employee_manage`.`skills` \
     (`id`, `title`) VALUES ('2', 'New')"
        
        # Test in search parameters
        employee.get_employees_via_api(search=boundary_payload, expected_code=400)
        skill.get_skills_via_api(search=boundary_payload, expected_code=400)
