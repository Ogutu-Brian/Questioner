from .import (UserCollection, QuestionCollection,
              RsvpCollection, MeetupCollection)


class Database(object):
    """Class that cotains all the database Schema"""

    def __init__(self):
        self.users = UserCollection()
        self.meetups = MeetupCollection()
        self.questions = QuestionCollection()
        self.rsvps = RsvpCollection()

    def tear_down(self):
        """Clears all the data from the database"""
        self.users.clear()
        self.meetups.clear()
        self.questions.clear()
        self.rsvps.clear()
