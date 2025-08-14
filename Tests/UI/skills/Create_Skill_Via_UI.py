import pytest
from data.skills import create_test_skill_UI

class CreateSkillViaUI:
    """Example UI tests that run with browser (not headless)"""

    SKILL = create_test_skill_UI()
    
    @pytest.mark.ui
    def test_browser_title(self, driver):
        """Test that browser opens and can navigate to a page"""
        # Navigate to a test page
        self.SKILL.create_skill_via_ui(driver)
    
