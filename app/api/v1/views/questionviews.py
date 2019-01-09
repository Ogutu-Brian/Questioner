from .import (question_view, status, db, Question)
from flask import jsonify, request
import json


@question_view.route('/questions', methods=["POST"])
def create_meetup():
    if request.is_json:
        valid, errors = db.questions.is_valid(request.json)
        if not valid:
            return jsonify({
                "message": "You encountered {} errors".format(len(errors)),
                "data": errors,
                "status": status.invalid_data,
            }), status.invalid_data
        data = request.json
        created_by = data.get("createdBy")
        meetup = data.get("meetup")
        title = data.get("title")
        body = data.get("body")
        question = Question(created_by=created_by,
                            meet_up=meetup, title=title, body=body)
        db.questions.insert(question)
        return jsonify({
            "message": "Successfully created a meetup",
            "status": status.created
        }), status.created
    else:
        return jsonify({
            "message": "The data must be in JSOn",
            "status": status.not_json
        }), status.not_json
