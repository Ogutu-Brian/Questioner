from . import BaseModel
from datetime import date
from typing import Dict


class Rsvp(BaseModel):
    """Defines attributes specific to Rsvp object"""

    def __init__(self, id_="", creatd_om=date.today(), meetup="", user="", response=""):
        super().__init__(id_=id_, created_on=creatd_om)
        self.meetup = meetup
        self.user = user
        self.response = response
        self.primary = (self.meetup, self.user)

    def to_dictionary(self)->Dict:
        """Overrides the basemodel method to represent an Rsvp object in a dictionary format"""
        dict_data = {
            "id": self.id,
            "primaryKey": self.primary,
            "meetup": self.meetup,
            "user": self.user,
            "response": self.response
        }
        return dict_data
