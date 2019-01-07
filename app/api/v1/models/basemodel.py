class BaseModel:
    """Contains properties shared accorss all the models"""

    def __init__(self, id="", created_on=""):
        self.id = id
        self.created_on = created_on

    def to_dictionary(self):
        """Method to be overriden by child classes to convert objects to dictionary
        """
        return {
            "id": self.id,
            "createdOn": self.created_on
        }

    def created_date(self):
        """Reeturns date created as a formatted string"""
        return self.created_on.strftime('%d-%m-%Y')
        