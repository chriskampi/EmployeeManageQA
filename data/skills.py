from functions.skill import Skill
from time import time

def accountability():
    """
    Create and return an accountability skill instance.
    
    Returns:
        Skill: An accountability skill with predefined attributes
    """
    skill = Skill()
    skill.set_id(5)
    skill.set_title("Accountability")

    return skill

def management():
    """
    Create and return a management skill instance.
    
    Returns:
        Skill: A management skill with predefined attributes
    """
    skill = Skill()
    skill.set_id(4)
    skill.set_title("Management")

    return skill

def logistics():
    """
    Create and return a logistics skill instance.
    
    Returns:
        Skill: A logistics skill with predefined attributes
    """
    skill = Skill()
    skill.set_id(8)
    skill.set_title("Logistics")

    return skill

def create_test_skill():
    """
    Create and return a test skill instance with a unique title.
    
    Returns:
        Skill: A test skill with unique attributes for testing purposes
    """
    skill = Skill()
    skill.set_title(f"Test Skill_{time()}")

    return skill

def create_test_skill_UI():
    """
    Create and return a UI test skill instance with a unique title.
    
    Returns:
        Skill: A UI test skill with unique attributes for UI testing
    """
    skill = Skill()
    skill.set_title(f"UI Skill_{time()}")

    return skill