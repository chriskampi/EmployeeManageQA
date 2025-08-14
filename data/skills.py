from functions.skill import Skill
from time import time

def accountability():

    skill = Skill()
    skill.set_id(5)
    skill.set_title("Accountability")

    return skill

def management():

    skill = Skill()
    skill.set_id(4)
    skill.set_title("Management")

    return skill

def logistics():

    skill = Skill()
    skill.set_id(8)
    skill.set_title("Logistics")

    return skill

def create_test_skill():

    skill = Skill()
    skill.set_title(f"Test Skill_{time()}")

    return skill

def create_test_skill_UI():

    skill = Skill()
    skill.set_title(f"UI Skill_{time()}")

    return skill