from . import BaseModel
import datetime
from typing import Dict


class User(BaseModel):
    """A model for user information"""

    def __init__(self, id_="", created_on=datetime.date.today(), first_name="", last_name="",
                 other_name="", email="", phone_number="", user_name="", is_admin=False, password=""):
        super().__init__(id_=id_, created_on=created_on)
        self.first_name = first_name
        self.last_name = last_name
        self.other_name = other_name
        self.email = email
        self.phone_number = phone_number
        self.user_name = user_name
        self.registred = self.created_date()
        self.is_admin = is_admin
        self.password = password

    def __str__(self):
        return self.first_name + " "+self.last_name

    def to_dictionary(self)->Dict:
        """Overrides the basemodel's method to present user object data in dictionary format"""
        dict_data = {
            "id": self.id,
            "firstname": self.first_name,
            "lastname": self.last_name,
            "othername": self.other_name,
            "email": self.email,
            "phoneNumber": self.phone_number,
            "username": self.user_name,
            "regustered": self.registred,
            "isAdmin": self.is_admin
        }
        return dict_data
