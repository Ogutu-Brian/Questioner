from flask import (Flask, jsonify, request)
from instance.config import secret_key
from .import user_view, meetup_view, question_view, status


def create_app():
    """Main flask appication"""
    app = Flask(__name__)
    app.secret_key = secret_key
    app.register_blueprint(user_view, url_prefix="/api/v1/users")
    app.register_blueprint(meetup_view, url_prefix="/api/v1")
    app.register_blueprint(question_view, url_prefix="/api/v1")
    return app


app = create_app()
if __name__ == "__main__":
    app.run()
