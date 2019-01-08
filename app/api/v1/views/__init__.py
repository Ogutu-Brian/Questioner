from app.api.v1.schema.db import Database
from flask import Blueprint
db = Database()
user_view = Blueprint('views.user_views', '__name__')
