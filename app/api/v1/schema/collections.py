from .import User, Question, Meetup, Rsvp


class BaseCollection(object):
    """Defines the shared database operations"""

    def __init__(self):
        self.index = 0
        self.data = {}
        self.errors = []

    def insert(self, item):
        """Allows for insertion of an item into the database"""
        item.id = self.index
        self.data[item.id] = item
        self.index += 1

    def query_all(self):
        """Queries all the data from the database"""
        return self.data

    def query_by_field(self, field, value):
        """Query an item by a given field value"""
        if field not in self.data[0].to_dictionary():
            """Checkiing if the field value given actually exist"""
            print("Item with field {} does not exist".format(field))
            return None
        for item in self.data.values():
            if item.to_dictionary().get(field) == value:
                return item
        return None

    def is_valid(self, item):
        """Checks for validity of data being iserted into the database, it is to be 
        overridden by child classes
        """
        errors = []
        return len(errors) == 0, self.errors

    def clear(self):
        """Clears every content of the database"""
        self.data = {}


class UserCollection(BaseCollection):
    """Overrides the methods from base collection to achieve feasible operations on User data"""

    def is_valid(self, item):
        errors = []
        if not item.get("id"):
            errors.append({
                "message": "id must be provided"
            })
        if not item.get("firstname"):
            errors.append({
                "message": "First name must be provided"
            })
        if not item.get("lastname"):
            errors.append({
                "message": "Last name must be provided"
            })
        if not item.get("email"):
            errors.append({
                "message": "email must be provided"
            })
        else:
            for object_ in self.data.values():
                if object_.to_dictionary().get("email") == item.get("email"):
                    errors.append({
                        "message": "The email address has already been taken"
                    })
        if not item.get("phoneNumber"):
            errors.append({
                "message": "Phone number must be provided"
            })
        if not item.get("username"):
            errors.append({
                "message": "username must be provided"
            })
        else:
            for object_ in self.data.values():
                if object_.to_dictionary().get("username") == item.get("username"):
                    errors.append({
                        "message": "The username has already been taken"
                    })
                    break
        if not item.get("password"):
            errors.append({
                "message": "Password must be provided"
            })
        return len(errors) == 0,errors
