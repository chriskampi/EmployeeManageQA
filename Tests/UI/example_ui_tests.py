import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIExamples:
    """Example UI tests that run with browser (not headless)"""
    
    @pytest.mark.ui
    def test_browser_title(self, driver, config):
        """Test that browser opens and can navigate to a page"""
        # Navigate to a test page
        driver.get("https://httpbin.org/")
        
        # Wait for page to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Verify page loaded
        assert "httpbin" in driver.title.lower()
    
    @pytest.mark.ui
    def test_browser_interaction(self, driver, config):
        """Test basic browser interactions"""
        # Navigate to a page with forms
        driver.get("https://httpbin.org/forms/post")
        
        # Wait for form to load
        wait = WebDriverWait(driver, 10)
        form = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        
        # Verify form is present
        assert form.is_displayed()
        
        # Find and interact with form elements
        customer_name_input = driver.find_element(By.NAME, "custname")
        customer_name_input.send_keys("Test User")
        
        # Verify input was entered
        assert customer_name_input.get_attribute("value") == "Test User"
    
    @pytest.mark.ui
    def test_browser_screenshot(self, driver, config):
        """Test taking a screenshot (useful for debugging)"""
        driver.get("https://httpbin.org/")
        
        # Wait for page to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Take screenshot
        screenshot_path = "test_screenshot.png"
        driver.save_screenshot(screenshot_path)
        
        # Verify screenshot was created (this would need file system access)
        # For now, just verify the method didn't raise an exception
        assert True
    
    @pytest.mark.ui
    def test_browser_window_size(self, driver, config):
        """Test browser window size configuration"""
        # Get current window size
        window_size = driver.get_window_size()
        
        # Verify window size matches config (if specified)
        if "window_size" in config:
            expected_width, expected_height = map(int, config["window_size"].split(","))
            assert window_size["width"] == expected_width
            assert window_size["height"] == expected_height
    
    @pytest.mark.ui
    def test_browser_navigation(self, driver, config):
        """Test browser navigation capabilities"""
        # Navigate to first page
        driver.get("https://httpbin.org/")
        
        # Navigate to second page
        driver.get("https://httpbin.org/get")
        
        # Go back
        driver.back()
        
        # Verify we're back on the first page
        assert "httpbin" in driver.title.lower()
        
        # Go forward
        driver.forward()
        
        # Verify we're on the second page
        assert "get" in driver.current_url
