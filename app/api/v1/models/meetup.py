from . import BaseModel
import datetime
from typing import Dict


class Meetup(BaseModel):
    """Defines the properties specific to a Meetup"""

    def __init__(self, id_="", created_on=datetime.date.today(), location="", images=[],
                 topic="", happening_on="", tags=[], creaed_by=""):
        super().__init__(id_=id_, created_on=created_on)
        self.topic = topic
        self.happening_on = happening_on
        self.tags = tags
        self.location = location
        self.images = images
        self.created_by = creaed_by

    def to_dictionary(self)->Dict:
        """
        Overrides the method from Basemodel to convert object properties into a dictionary
        data structure
        """
        return {
            "id": self.id,
            "createdOn": self.created_date(),
            "location": self.location,
            "images": self.images,
            "topic": self.topic,
            "happendingOn": self.happening_on,
            "tags": self.tags,
        }
