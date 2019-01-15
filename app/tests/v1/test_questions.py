from . import (client, user_data, meetup_data, QuestionData,
               question_data, user_data, meetup_data, db)
from app.api.v1.views import status
import unittest
import json


class TestQuestion(unittest.TestCase):
    """Class for testing operations on Question records"""

    def post_data(self, url="", data={}, headers={}):
        """Posts data to various endpoints"""
        data = json.dumps(data)
        result = client().post(url, data=data, headers=headers)
        return json.loads(result.get_data(as_text=True))

    def test_correct_question_post(self):
        """tests for correct creation of question"""
        question_data = QuestionData()
        db.tear_down()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        question_data.valid_question_data["data"]["meetup"] = meetup_id
        question_data.valid_question_data["data"]["createdBy"] = user_id
        result = self.post_data(url=question_data.valid_question_data.get("url"), data=question_data.valid_question_data.get(
            "data"), headers=question_data.valid_question_data.get("headers"))
        self.assertEqual(status.created, result.get("status"))

    def test_non_json_data(self):
        """Tests for data that is not in json format"""
        question_data = QuestionData()
        db.tear_down()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        question_data.valid_question_data["headers"] = ""
        question_data.valid_question_data["meetup"] = meetup_id
        question_data.valid_question_data["createdBy"] = user_id
        result = self.post_data(url=question_data.valid_question_data.get("url"), data=question_data.valid_question_data.get(
            "data"), headers=question_data.valid_question_data.get("headers"))
        self.assertEqual(status.not_json, result.get("status"))

    def test_missing_creator(self):
        """tests fir data that does not contain creator of the question"""
        question_data = QuestionData()
        db.tear_down()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        question_data.missing_creator_data["meetup"] = meetup_id
        result = self.post_data(url=question_data.missing_creator_data.get("url"), data=question_data.missing_creator_data.get(
            "data"), headers=question_data.missing_creator_data.get("headers"))
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_body(self):
        """Tests for missing body during creation of a question"""
        db.tear_down()
        question_data = QuestionData()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        question_data.missing_body_data["createdBy"] = user_id
        question_data.missing_body_data["meetup"] = meetup_id
        result = self.post_data(url=question_data.missing_body_data.get("url"), data=question_data.missing_body_data.get(
            "data"), headers=question_data.missing_body_data.get("headers"))
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_meetup(self):
        """Tests for Question that is not linked to a meetup"""
        db.tear_down()
        question_data = QuestionData()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        question_data.missing_meetup_data["createdBy"] = user_id
        result = self.post_data(url=question_data.missing_meetup_data.get("url"), data=question_data.missing_meetup_data.get(
            "data"), headers=question_data.missing_meetup_data.get("headers"))
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_invalid_user(self):
        """Tests if a user with an id exists in the database"""
        question_data = QuestionData()
        db.tear_down()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, user.get("status"))
        question_data.invalid_user_data["meetup"] = meetup_id
        result = self.post_data(url=question_data.invalid_user_data.get("url"), data=question_data.invalid_user_data.get(
            "data"), headers=question_data.invalid_user_data.get("headers"))
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_invalid_meetup(self):
        """Tests if a meetup with the given id exists in the database"""
        question_data = QuestionData()
        db.tear_down()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        question_data.invalid_meetup_data["createdBy"] = user_id
        result = self.post_data(url=question_data.invalid_meetup_data.get("url"), data=question_data.invalid_meetup_data.get(
            "data"), headers=question_data.invalid_meetup_data.get("headers"))
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_successful_upvote(self):
        """Tests the endpoint for upvoting a question in questioner"""
        question_data = QuestionData()
        db.tear_down()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        question_data.valid_upvote_data["data"]["meetup"] = meetup_id
        question_data.valid_upvote_data["data"]["createdBy"] = user_id
        question = self.post_data(url=question_data.valid_upvote_data.get(
            "url"), data=question_data.valid_upvote_data.get("data"), headers=question_data.valid_upvote_data.get("headers"))
        self.assertEqual(status.created, question.get("status"))
        question_id = question.get("data")[0].get("id")
        url = "/api/v1/questions/{}/upvote".format(question_id)
        result = json.loads(client().patch(url).get_data(as_text=True))
        self.assertEqual(status.created, result.get("status"))

    def test_unexsiting_upvote_question(self):
        """Tests for a patch to a question that does not exist"""
        db.tear_down()
        question_data = QuestionData()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        question_data.unexsiting_query_upvote_data["data"]["createdBy"] = user_id
        question_data.unexsiting_query_upvote_data["data"]["meetup"] = meetup_id
        question = self.post_data(url=question_data.unexsiting_query_upvote_data.get(
            "url"), data=question_data.unexsiting_query_upvote_data.get("data"), headers=question_data.unexsiting_query_upvote_data.get("headers"))
        self.assertEqual(status.created, question.get("status"))
        url = "/api/v1/questions/-1/upvote"
        result = json.loads(client().patch(url).get_data(as_text=True))
        self.assertGreaterEqual(status.not_found, result.get("status"))

    def test_successful_downvote(self):
        """Tests the endpoint for downvoting a question in Questioner"""
        question_data = QuestionData()
        db.tear_down()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        question_data.valid_downvote_data["data"]["createdBy"] = user_id
        question_data.valid_downvote_data["data"]["meetup"] = meetup_id
        question = self.post_data(url=question_data.valid_downvote_data.get(
            "url"), data=question_data.valid_downvote_data.get("data"), headers=question_data.valid_downvote_data.get("headers"))
        self.assertEqual(status.created, question.get("status"))
        question_id = question.get("data")[0].get("id")
        url = "/api/v1/questions/{}/downvote".format(question_id)
        result = json.loads(client().patch(url).get_data(as_text=True))
        self.assertEqual(status.created, result.get("status"))

    def test_unexisting_downvote_question(self):
        """Tests if the question being downvotest is not existing"""
        question_data = QuestionData()
        db.tear_down()
        data = meetup_data.valid_meetup_data.get("data")
        headers = meetup_data.valid_meetup_data.get("headers")
        url = meetup_data.valid_meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        question_data.unexsiting_query_upvote_data["data"]["createdBy"] = user_id
        question_data.unexsiting_query_upvote_data["data"]["meetup"] = meetup_id
        question = self.post_data(url=question_data.unexsiting_query_upvote_data.get(
            "url"), data=question_data.unexsiting_query_upvote_data.get("data"), headers=question_data.unexsiting_query_upvote_data.get("headers"))
        self.assertEqual(status.created, question.get("status"))
        url = "/api/v1/questions/-1/downvote"
        result = json.loads(client().patch(url).get_data(as_text=True))
        self.assertEqual(status.not_found, result.get("status"))


if __name__ == "__main__":
    unittest.main(exit=False)
