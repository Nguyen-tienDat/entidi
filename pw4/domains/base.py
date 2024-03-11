class Base:
    def __init__(self, _id=0, name='', dob=''):
        self.id = _id
        self.name = name
        self.dob = dob

    def _get_name(self):
        return self.name

    def _set_name(self, name):
        self.name = name

    def _get_id(self):
        return self.id

    def _set_id(self, _id):
        self.id = _id

    def _get_dob(self):
        return self.dob

    def _set_dob(self, dob):
        self.dob = dob
