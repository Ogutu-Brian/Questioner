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

    @app.errorhandler(404)
    def page_not_found_handler(error):
        """Handles page not found errors e.g invalid urls"""
        return jsonify({
            "message": "The requested url was not found, plese double check",
            "status": status.not_found
        }), status.not_found
    return app

    @app.errorhandler(405)
    def method_not_allowed_handler(error):
        """ Handles invalid methods for existing endpoints or urls"""
        if request.method == "POST":
            return jsonify({
                "message": "You could be doing a post instead of a get",
                "status": status.method_not_allowed
            }), status.method_not_allowed
        else:
            return jsonify({
                "message": "You could be doing a get request instead of a post",
                "status": status.method_not_allowed
            }), status.method_not_allowed


app = create_app()
if __name__ == "__main__":
    app.run()
