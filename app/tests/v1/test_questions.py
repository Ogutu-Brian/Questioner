from . import (client, user_data, meetup_data, question_data, db)
from app.api.v1.views import status
import unittest
import json


class TestQuestion(unittest.TestCase):
    """Class for testing operations on Question records"""

    def create_question(self, url="", data={}, headers={}):
        """Creates a user and a meetup and creartes questions using those details"""
        data = json.dumps(data)
        result = client().post(url, data=data, headers=headers)
        return json.loads(result.get_data(as_text=True))

    def test_correct_question_post(self):
        """tests for correct creation of question"""
        client().post(user_data.get("sign_up_url"),
                      data=json.dumps(user_data.get("sign_up")), headers=user_data.get("headers"))
        client().post(meetup_data.get("url"), data=json.dumps(meetup_data.get(
            "data")), headers=meetup_data.get("headers"))
        result = self.create_question(url=question_data.get(
            "url"), data=question_data.get("data"), headers=question_data.get("headers"))
        self.assertEqual(status.created, result.get("status"))

    def test_unexisting_user(self):
        """tests for creation of a question by a non user"""
        test_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "title": "Responnsive Web design",
                "createdBy": 2,
                "response": "yes",
                "body": "What is the best way of getting around responsiveness of a website",
                "meetup": 1
            },
            "url": "/api/v1/questions"
        }
        client().post(user_data.get("sign_up_url"),
                      data=json.dumps(user_data.get("sign_up")), headers=user_data.get("headers"))
        client().post(meetup_data.get("url"), data=json.dumps(meetup_data.get(
            "data")), headers=meetup_data.get("headers"))
        result = self.create_question(url=question_data.get(
            "url"), data=test_data.get("data"), headers=test_data.get("headers"))
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_unexisting_meetup(self):
        """tests for posting of a question to a meetup that does not exist"""
        test_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "title": "Responnsive Web design",
                "createdBy": 1,
                "response": "yes",
                "body": "What is the best way of getting around responsiveness of a website",
                "meetup": 2
            },
            "url": "/api/v1/questions"
        }
        client().post(user_data.get("sign_up_url"),
                      data=json.dumps(user_data.get("sign_up")), headers=user_data.get("headers"))
        client().post(meetup_data.get("url"), data=json.dumps(meetup_data.get(
            "data")), headers=meetup_data.get("headers"))
        result = self.create_question(url=test_data.get(
            "url"), data=test_data.get("data"), headers=test_data.get("headers"))
        self.assertEqual(status.invalid_data, result.get("status"))
