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
        if field not in self.data[0].to_json_string():
            """Checkiing if the field value given actually exist"""
            self.errors.append(
                "Item with field {} does not exist".format(field))
            return None
        for item in self.data.values():
            if item.to_dict_string().get(field) == value:
                return item
        return None

    def is_valid(self):
        """Checks for validity of data being iserted into the database, it is to be 
        overridden by child classes
        """
        return len(self.errors) == 0, self.errors

    def clear(self):
        """Clears every content of the database"""
        self.data = {}
