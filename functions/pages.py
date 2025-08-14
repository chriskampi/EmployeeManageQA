from locators.pages.employees import EmployeePage
from locators.pages.login import LoginPage
from locators.pages.skills import SkillPage


def navigate_to_employees_page(driver):
    """Navigate to employees page and return EmployeePage instance"""
    employee_page = EmployeePage(driver)
    driver.get(employee_page.url)
    return employee_page


def navigate_to_login_page(driver):
    """Navigate to login page and return LoginPage instance"""
    login_page = LoginPage(driver)
    driver.get(login_page.url)
    return login_page


def navigate_to_skills_page(driver):
    """Navigate to skills page and return SkillPage instance"""
    skill_page = SkillPage(driver)
    driver.get(skill_page.url)
    return skill_page
