from .import BaseModel
from datetime import date
from typing import Dict


class Question(BaseModel):
    """Defines the properties specific to a Question object"""

    def __init__(self, id_="", created_on=date.today(), created_by="", meet_up="",
                 title="", body="", votes=""):
        super().__init__(id_=id_, created_on=created_on)
        self.created_by = created_by
        self.meet_up = meet_up
        self.title = title
        self.body = body
        self.votes = votes

    def to_dictionary(self)->Dict:
        """
        Overrides the BaseModel's method to return a dictionary representation of question
        object
        """
        dictionary_data = {
            "id": self.id,
            "createdOn": self.created_on,
            "createdBy": self.created_by,
            "meetup": self.meet_up,
            "title": self.meet_up,
            "body": self.body,
            "votes": self.votes
        }
        return dictionary_data
