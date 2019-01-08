from app.api.v1.schema.db import Database
from flask import Blueprint
from app.api.v1.models.usermodel import User

db = Database()
user_view = Blueprint('views.user_views', '__name__')
