from flask import (Flask)
from instance.config import secret_key
from .import user_view


def create_app():
    """Main flask appication"""
    app = Flask(__name__)
    app.secret_key = secret_key
    app.register_blueprint(user_view, url_prefix="/api/v1/users")
    return app


app = create_app()
if __name__ == "__main__":
    app.run()
