from . import (client, user_data, meetup_data, question_data)
from app.api.v1.views import status
import unittest
import json


class TestQuestion(unittest.TestCase):
    """Class for testing operations on Question records"""

    def create_question(self, url="", data={}, headers={}):
        """Creates a user and a meetup and creartes questions using those details"""
        data = json.dumps(data)
        client().post(user_data.get("sign_up_url"),
                      data=json.dumps(user_data.get("sign_up")), headers=user_data.get("headers"))
        client().post(meetup_data.get("url"), data=json.dumps(meetup_data.get(
            "data")), headers=meetup_data.get("headers"))
        result = client().post(url, data=data, headers=headers)
        return json.loads(result.get_data(as_text=True))

    def test_correct_question_post(self):
        result = self.create_question(url=question_data.get(
            "url"), data=question_data.get("data"), headers=question_data.get("headers"))
        self.assertEqual(status.created, result.get("status"))

    def test_unexisting_user(self):
        """tests for a user that is not in the system"""
        question_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "title": "Responnsive Web design",
                "createdBy": 4,
                "response": "yes",
                "body": "What is the best way of getting around responsiveness of a website",
                "meetup": 5
            },
            "url": "/api/v1/questions"
        }
        result = self.create_question(url=question_data.get(
            "url"), data=question_data.get("data"), headers=question_data.get("headers"))
        self.assertEqual(status.invalid_data, result.get("status"))
