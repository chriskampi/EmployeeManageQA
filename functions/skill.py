import requests
import conftest
from conftest import load_config
from functions import pages
import time

class Skill:
    def __init__(self, id=None, title=None):
        self._id = id
        self._title = title
        self.base_url = load_config()["api_base_url"]

    # Setters
    def set_id(self, id):
        self._id = id

    def set_title(self, title):
        self._title = title

    # Getters
    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_skills_via_api(self, search=None, expected_code=200, time=1, expected_skills=None):
        """
        Test the GET /getSkills endpoint
        
        Args:
            search: Optional search term for filtering skills
            expected_code: Expected HTTP status code (default: 200)
            time: Request timeout in seconds (default: 1)
            expected_skills: List of expected skill dictionaries to validate against
        """
        url = f"{self.base_url}/api/skills/getSkills"
        params = {}
        if search:
            params['search'] = search
            
        response = requests.get(url, params=params, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Skills fetched successfully'
            assert 'data' in response_data
            assert isinstance(response_data['data'], list)
            
            # Validate each skill structure
            for skill in response_data['data']:
                assert 'id' in skill
                assert 'title' in skill
                
            # If expected_skills is provided, validate the response matches
            if expected_skills is not None:
                # Build the expected response structure
                expected_response = {
                    "success": True,
                    "message": "Skills fetched successfully",
                    "data": expected_skills
                }
                
                # Assert the response matches the expected structure
                assert response_data == expected_response, \
                    f"Response does not match expected structure. Expected: {expected_response}, Got: {response_data}"
                
        return response

    def create_skill_via_api(self, expected_code=200, time=1):
        """
        Test the POST /createSkill endpoint
        """
        url = f"{self.base_url}/api/skills/createSkill"
        payload = {
            "title": self.get_title()
        }
        
        response = requests.post(url, json=payload, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Skill created successfully'
            assert 'data' in response_data
            
            data = response_data['data']
            assert 'id' in data
            assert data['title'] == self.get_title()
            
            # Set the skill ID from response
            self.set_id(data['id'])
            
        return response

    def update_skill_via_api(self, skill_data, expected_code=200, time=1):
        """
        Test the PUT /updateSkill endpoint
        """
        url = f"{self.base_url}/api/skills/updateSkill"
        payload = {
            "id": self.get_id(),
            "title": skill_data.get('title')
        }
        
        response = requests.put(url, json=payload, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Skill updated successfully'
            assert 'data' in response_data
            
            data = response_data['data']
            assert data['id'] == self.get_id()
            assert data['title'] == skill_data.get('title')
            
            # Update the skill object with new data
            self.set_title(skill_data.get('title'))
            
        return response

    def delete_skill_via_api(self, expected_code=200, time=1):
        """
        Test the DELETE /deleteSkill endpoint
        """
        url = f"{self.base_url}/api/skills/deleteSkill"
        params = {"id": self.get_id()}
        
        response = requests.delete(url, params=params, timeout=time)
        assert response.status_code == expected_code
        
        if expected_code == 200:
            response_data = response.json()
            assert response_data['success'] == True
            assert response_data['message'] == 'Skill deleted successfully'
            
        return response

    # Page Object Functions for UI Testing

    def create_skill_via_ui(self, driver):
        """Create skill via UI using page object and paths"""
        skill_page = pages.navigate_to_skills_page(driver)
        
        skill_page.container.click_button_add_entity()
        # Fill in skill form using page object paths
        skill_page.set_text_input_skill_title(self.get_title())
        skill_page.container.click_button_save_entity()

    def delete_skill_via_ui(self, driver):
        """delete skill via UI using page object and paths"""
        skill_page = pages.navigate_to_skills_page(driver)

        skill_page.container.click_button_delete_entity(self.get_title())
        driver.refresh()
        skill_page.container.validate_tr_entity_row_info(self.get_title(), False)
