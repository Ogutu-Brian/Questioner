from typing import Dict
from datetime import date


class BaseModel(object):
    """Contains properties shared accorss all the models"""

    def __init__(self, id_="", created_on=date.today()):
        self.id = id_
        self.created_on = created_on

    def to_dictionary(self)->Dict:
        """Method to be overriden by child classes to return object properties in to dictionary
        format
        """
        return {
            "id": self.id,
            "createdOn": self.created_on
        }

    def created_date(self):
        """Reeturns date created as a formatted string (day-month-year) if date is provided"""
        if self.created_on:
            return self.created_on.strftime('%d-%m-%Y')
        return self.created_date
