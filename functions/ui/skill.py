class Skill:
    def __init__(self, id=None, title=None):
        self._id = id
        self._title = title

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