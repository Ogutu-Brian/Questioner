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
        db.tear_down()
        return json.loads(result.get_data(as_text=True))

    def test_correct_question_post(self):
        """tests for correct creation of question"""
        result = self.create_question(url=question_data.get(
            "url"), data=question_data.get("data"), headers=question_data.get("headers"))
        self.assertEqual(status.created, result.get("status"))

    def test_non_json_data(self):
        """Tests for data that is not in json format"""
        question_data = {
            "headers": {
                # "Content-Type": "application/json"
            },
            "data": {
                "title": "Responnsive Web design",
                "createdBy": 1,
                "body": "What is the best way of getting around responsiveness of a website",
                "meetup": 3
            },
            "url": "/api/v1/questions"
        }
        result = self.create_question(url=question_data.get(
            "url"), data=question_data.get("data"), headers=question_data.get("headers"))
        print(result)
        self.assertEqual(status.not_json, result.get("status"))

    def test_missing_creator(self):
        """tests fir data that does not contain creator of the question"""
        question_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "title": "Responnsive Web design",
                # "createdBy": 1,
                "body": "What is the best way of getting around responsiveness of a website",
                "meetup": 3
            },
            "url": "/api/v1/questions"
        }
        result = self.create_question(url=question_data.get(
            "url"), data=question_data.get("data"), headers=question_data.get("headers"))
        print(result)
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_body(self):
        """Tests for missing body during creation of a question"""
        question_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "title": "Responnsive Web design",
                "createdBy": 1,
                # "body": "What is the best way of getting around responsiveness of a website",
                "meetup": 1
            },
            "url": "/api/v1/questions"
        }
        result = self.create_question(url=question_data.get(
            "url"), data=question_data.get("data"), headers=question_data.get("headers"))
        print(result)
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_meetup(self):
        """Tests for Question that is not linked to a meetup"""
        question_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "title": "Responnsive Web design",
                "createdBy": 1,
                "body": "What is the best way of getting around responsiveness of a website",
                # "meetup": 3
            },
            "url": "/api/v1/questions"
        }
        result = self.create_question(url=question_data.get(
            "url"), data=question_data.get("data"), headers=question_data.get("headers"))
        print(result)
        self.assertEqual(status.invalid_data, result.get("status"))
