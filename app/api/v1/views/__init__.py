from app.api.v1.schema.db import Database
from flask import Blueprint
from app.api.v1.models.usermodel import User
from app.api.v1.models.meetup import Meetup


class Status(object):
    """Defines my status codes"""

    def __init__(self):
        self.not_json = 422
        self.created = 201
        self.invalid_data = 406
        self.success = 200


status = Status()

db = Database()
user_view = Blueprint('views.userviews', '__name__')
meetup_view = Blueprint('views.meetupviews', '__name__')
