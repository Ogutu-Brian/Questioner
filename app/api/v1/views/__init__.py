from app.api.v1.schema.db import Database
from flask import Blueprint
from app.api.v1.models.usermodel import User
from app.api.v1.models.meetup import Meetup
from app.api.v1.models.question import Question
from app.api.v1.models.rsvp import Rsvp


class Status(object):
    """Defines my status codes"""

    def __init__(self):
        self.not_json = 422
        self.created = 201
        self.invalid_data = 406
        self.success = 200
        self.not_found = 404
        self.no_content = 204


status = Status()

db = Database()
user_view = Blueprint('views.userviews', '__name__')
meetup_view = Blueprint('views.meetupviews', '__name__')
question_view = Blueprint('views.questionviews', '__name__')
