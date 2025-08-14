import pytest
import requests
from typing import Dict, Any

class TestAPIExamples:
    """Example API tests that run without browser (headless)"""
    
    @pytest.mark.api
    def test_api_status(self, config: Dict[str, Any]):
        """Test API endpoint status using requests library"""
        api_url = config["api_base_url"]
        response = requests.get(f"{api_url}/status/200")
        
        assert response.status_code == 200
        # The /status/200 endpoint doesn't return JSON, just a 200 status
    
    @pytest.mark.api
    def test_api_get_request(self, config: Dict[str, Any]):
        """Test GET request to API endpoint"""
        api_url = config["api_base_url"]
        response = requests.get(f"{api_url}/get", params={"test": "value"})
        
        assert response.status_code == 200
        data = response.json()
        assert data["args"]["test"] == "value"
    
    @pytest.mark.api
    def test_api_post_request(self, config: Dict[str, Any]):
        """Test POST request to API endpoint"""
        api_url = config["api_base_url"]
        test_data = {"name": "John Doe", "email": "john@example.com"}
        
        response = requests.post(f"{api_url}/post", json=test_data)
        
        assert response.status_code == 200
        data = response.json()
        assert data["json"]["name"] == "John Doe"
        assert data["json"]["email"] == "john@example.com"
    
    @pytest.mark.api
    def test_api_headers(self, config: Dict[str, Any]):
        """Test API headers functionality"""
        api_url = config["api_base_url"]
        custom_headers = {"X-Custom-Header": "test-value"}
        
        response = requests.get(f"{api_url}/headers", headers=custom_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["headers"]["X-Custom-Header"] == "test-value"
    
    @pytest.mark.api
    def test_api_response_time(self, config: Dict[str, Any]):
        """Test API response time"""
        api_url = config["api_base_url"]
        
        response = requests.get(f"{api_url}/delay/1")
        
        assert response.status_code == 200
        # Note: This test will take ~1 second due to the delay endpoint
