from sys import maxsize
class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, id=None):
        self.firstname = first_name
        self.middlename = middle_name
        self.lastname = last_name
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname, self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

