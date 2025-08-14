from functions.skill import Skill

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
    skill.set_title("Test Skill")

    return skill