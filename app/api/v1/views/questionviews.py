from .import (question_view, status, db, Question)
from flask import jsonify, request
import json


@question_view.route('/questions', methods=["POST"])
def create_question():
    """A post endpoint for creating a question for a given meetup"""
    response = None
    if request.is_json:
        valid, errors = db.questions.is_valid(request.json)
        if not valid:
            response = jsonify({
                "message": "You encountered {} errors".format(len(errors)),
                "data": errors,
                "status": status.invalid_data,
            }), status.invalid_data
        else:
            data = request.json
            created_by = data.get("createdBy")
            meetup = data.get("meetup")
            title = data.get("title")
            body = data.get("body")
            if not db.users.query_by_field("id", created_by):
                response = jsonify({
                    "message": "A user with that id does not exist",
                    "status": status.invalid_data
                }), status.invalid_data
            elif not db.meetups.query_by_field("id", meetup):
                response = jsonify({
                    "message": "A meetup with that id does not exist",
                    "status": status.invalid_data
                }), status.invalid_data
            else:
                question = Question(created_by=created_by,
                                    meet_up=meetup, title=title, body=body)
                db.questions.insert(question)
                response = jsonify({
                    "message": "Successfully created a question",
                    "data": [question.to_dictionary()],
                    "status": status.created
                }), status.created
    else:
        response = jsonify({
            "message": "The data must be in JSOn",
            "status": status.not_json
        }), status.not_json
    return response


@question_view.route('/questions/<question_id>/upvote', methods=["PATCH"])
def upvote(question_id):
    """Increates a question's vote by 1"""
    response = None
    question = db.questions.query_by_field("id", int(question_id))
    if not question:
        response = jsonify({
            "message": "A question with that id does not exist",
            "status": status.not_found
        }), status.not_found
    else:
        question.votes += 1
        response = jsonify({
            "message": "successfully upvoted",
            "status": status.created,
            "data": [question.to_dictionary()]
        }), status.created
    return response


@question_view.route('/questions/<question_id>/downvote', methods=["PATCH"])
def downvote(question_id):
    """Decreases the votes by 1"""
    response = None
    question = db.questions.query_by_field("id", int(question_id))
    if not question:
        response = jsonify({
            "message": "A question with that id does not exist",
            "status": status.not_found
        }), status.not_found
    else:
        question.votes -= 1
        response = jsonify({
            "message": "Successfully downvoted",
            "status": status.created,
            "data": [question.to_dictionary()]
        }), status.created
    return response
