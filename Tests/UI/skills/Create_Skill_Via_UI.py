import pytest
from data.skills import create_test_skill_UI

class TestCreateSkillViaUI:
    """UI tests for creating skills via the web interface"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test data before each test"""
        self.skill = create_test_skill_UI()
    
    @pytest.mark.ui
    def test_create_skill_via_ui(self, driver, config):
        """Test creating a skill via the UI using page objects"""
        # Skip if not in UI mode
        if not driver:
            pytest.skip("UI test requires browser driver")
        
        # Create skill via UI using page object
        skill_page = self.skill.create_skill_via_ui(driver)
        
        # Add assertions here to verify the skill was created successfully
        # For example, check if the skill appears in the skills list
        assert skill_page is not None
        
    @pytest.mark.ui
    def test_skill_form_input(self, driver, config):
        """Test that skill form inputs work correctly"""
        # Skip if not in UI mode
        if not driver:
            pytest.skip("UI test requires browser driver")
        
        # Navigate to skills page
        from functions.pages import navigate_to_skills_page
        skill_page = navigate_to_skills_page(driver)
        
        # Test form input
        skill_page.set_text_input_skill_title("Test Skill Title")
        
        # Add assertions here to verify the input was entered correctly
        assert skill_page is not None
    
