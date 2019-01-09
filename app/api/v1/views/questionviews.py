from .import (question_view, status, db, Question)
from flask import jsonify, request
import json


@question_view.route('/questions', methods=["POST"])
def create_question():
    """A post endpoint for creating a question for a given meetup"""
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
            "message": "Successfully created a question",
            "data": [question.to_dictionary()],
            "status": status.created
        }), status.created
    else:
        return jsonify({
            "message": "The data must be in JSOn",
            "status": status.not_json
        }), status.not_json


@question_view.route('/questions/<question_id>/upvote', methods=["PATCH"])
def upvote(question_id):
    """Increates a question's vote by 1"""
    question = db.questions.query_by_field("id", int(question_id))
    if not question:
        return jsonify({
            "message": "A question with that id does not exist",
            "status": status.not_found
        }), status.not_found
    else:
        question.votes += 1
        return jsonify({
            "message": "successfully upvoted",
            "status": status.created,
            "data": [question.to_dictionary()]
        }), status.created


@question_view.route('/questions/<question_id>/downvote', methods=["PATCH"])
def downvote(question_id):
    """Decreases the votes by 1"""
    question = db.questions.query_by_field("id", int(question_id))
    if not question:
        return jsonify({
            "message": "A question with that id does not exist",
            "status": status.not_found
        }), status.not_found
    question.votes -= 1
    return jsonify({
        "message": "Successfully downvoted",
        "status": status.created,
        "data": [question.to_dictionary()]
    }), status.created
