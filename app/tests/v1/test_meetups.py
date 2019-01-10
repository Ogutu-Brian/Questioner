from .import (client, db, meetup_data, status, user_data)
import unittest
import json


class TestMeetup(unittest.TestCase):
    """Testst the operations performed on meetup records"""

    def post_data(self, url="", data={}, headers={}):
        """Posts data to various endpoints"""
        data = json.dumps(data)
        result = client().post(url, data=data, headers=headers)
        return json.loads(result.get_data(as_text=True))

    def create_rsvp(self, url="", data={}, headers={}):
        """Creates rsvp for testing"""
        data = json.dumps(data)
        result = client().post(url, data=data, headers=headers)
        return json.loads(result.get_data(as_text=True))

    def test_successful_meetup(self):
        """Tests for successful creation of a meetup"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        result = self.post_data(url=url, data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.created, result.get("status"))

    def test_missing_tags(self):
        """Tests for data that does not contain tags"""
        meetup_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "location": "Andela Campus",
                "images": ["/images/important", "/images/meetup"],
                "topic": "Responsive Web Design",
                # "Tags": ["User Interface", "Responsive Design"],
                "happeningOn": "2018-04-23T18:25:43.511Z"
            },
            "url": "/api/v1/meetups"
        }
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        result = self.post_data(url=url, data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_location(self):
        """tests for data that does not contain location of meetup"""
        meetup_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                # "location": "Andela Campus",
                "images": ["/images/important", "/images/meetup"],
                "topic": "Responsive Web Design",
                "Tags": ["User Interface", "Responsive Design"],
                "happeningOn": "2018-04-23T18:25:43.511Z"
            },
            "url": "/api/v1/meetups"
        }
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        result = self.post_data(url=url, data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_meetup_date(self):
        """Test data that does not contain meetup date"""
        meetup_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "location": "Andela Campus",
                "images": ["/images/important", "/images/meetup"],
                "topic": "Responsive Web Design",
                "Tags": ["User Interface", "Responsive Design"],
                # "happeningOn": "2018-04-23T18:25:43.511Z"
            },
            "url": "/api/v1/meetups"
        }
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        result = self.post_data(url=url, data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_images(self):
        """Image location is optional so missing in json object should not cause failure"""
        meetup_data = {
            "headers": {
                "Content-Type": "application/json"
            },
            "data": {
                "location": "Andela Campus",
                # "images": ["/images/important", "/images/meetup"],
                "topic": "Responsive Web Design",
                "Tags": ["User Interface", "Responsive Design"],
                "happeningOn": "2018-04-23T18:25:43.511Z"
            },
            "url": "/api/v1/meetups"
        }
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        result = self.post_data(url=url, data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.created, result.get("status"))

    def test_invalid_post_object(self):
        """Tests if the data being posted is actually json"""
        meetup_data = {
            "headers": {
                # "Content-Type": "application/json"
            },
            "data": {
                "location": "Andela Campus",
                "images": ["/images/important", "/images/meetup"],
                "topic": "Responsive Web Design",
                "Tags": ["User Interface", "Responsive Design"],
                "happeningOn": "2018-04-23T18:25:43.511Z"
            },
            "url": "/api/v1/meetups"
        }
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        result = self.post_data(url=url, data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.not_json, result.get("status"))

    def test_get_meetup_record(self):
        """Tests for get request for a specific meetup given a meetup id"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        get_url = "/api/v1/meetups/{}".format(meetup_id)
        result = json.loads(client().get(get_url).get_data(as_text=True))
        self.assertEqual(status.success, result.get("status"))
        db.tear_down()

    def test_get_all_meetup_records(self):
        """"Test for getting all meetups endoint"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        meetup1 = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup1.get("status"))
        meetup2 = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup2.get("status"))
        get_url = "/api/v1/meetups/upcoming/"
        result = json.loads(client().get(get_url).get_data(as_text=True))
        self.assertEqual(status.success, result.get("status"))
        db.tear_down()

    def test_nill_result(self):
        """tests for nill result when fetching all upcoming meetup records"""
        db.tear_down()
        url = "/api/v1/meetups/upcoming/"
        result = client().get(url)
        self.assertEqual(status.no_content, result.status_code)
        db.tear_down()

    def test_successful_rsvp_response(self):
        """Tests for a successful creation of rsvp by a user"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        rsvp_data = {
            "data": {
                "user": user_id,
                "response": "yes"
            },
            "url": "/api/v1/meetups/{}/rsvps".format(meetup_id)
        }
        result = self.create_rsvp(url=rsvp_data.get(
            "url"), data=rsvp_data.get("data"), headers=headers)
        self.assertEqual(status.created, result.get("status"))
        db.tear_down()

    def test_ivalid_meetup_for_rsvp(self):
        """Tests for invalid meetup id during creation of rsvp"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        #url = meetup_data.get("url")
        # meetup = self.post_data(url=url, data=data, headers=headers)
        # self.assertEqual(status.created, meetup.get("status"))
        # meetup_id = meetup.get("data")[0].get("id")
        meetup_id = 0
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        rsvp_data = {
            "data": {
                "user": user_id,
                "response": "yes"
            },
            "url": "/api/v1/meetups/{}/rsvps".format(meetup_id)
        }
        result = self.create_rsvp(url=rsvp_data.get(
            "url"), data=rsvp_data.get("data"), headers=headers)
        self.assertEqual(status.not_found, result.get("status"))
        db.tear_down()

    def test_ivalid_user_for_rsvp(self):
        """Tests for invalid user creating the rsvp"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        #url = user_data.get("sign_up_url")
        # user = self.post_data(url=url, data=data, headers=headers)
        # user_id = user.get("data")[0].get("id")
        # self.assertEqual(status.created, user.get("status"))
        user_id = 0
        rsvp_data = {
            "data": {
                "user": user_id,
                "response": "yes"
            },
            "url": "/api/v1/meetups/{}/rsvps".format(meetup_id)
        }
        result = self.create_rsvp(url=rsvp_data.get(
            "url"), data=rsvp_data.get("data"), headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))
        db.tear_down()

    def test_ivalid_rsvp_response(self):
        """Tests for response not in ["yes","no","maybe"]"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        rsvp_data = {
            "data": {
                "user": user_id,
                "response": "I might be there"
            },
            "url": "/api/v1/meetups/{}/rsvps".format(meetup_id)
        }
        result = self.create_rsvp(url=rsvp_data.get(
            "url"), data=rsvp_data.get("data"), headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))
        db.tear_down()

    def test_non_json_data_for_rsvp(self):
        """Tests if the post data for Rsvp is not json"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        headers = {}
        rsvp_data = {
            "data": {
                "user": user_id,
                "response": "yes"
            },
            "url": "/api/v1/meetups/{}/rsvps".format(meetup_id)
        }
        result = self.create_rsvp(url=rsvp_data.get(
            "url"), data=rsvp_data.get("data"), headers=headers)
        self.assertEqual(status.not_json, result.get("status"))
        db.tear_down()

    def test_missing_user_in_rsvp(self):
        """Tests if user id is not provided when creating rsvp"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        # url = user_data.get("sign_up_url")
        # user = self.post_data(url=url, data=data, headers=headers)
        # user_id = user.get("data")[0].get("id")
        #self.assertEqual(status.created, user.get("status"))
        rsvp_data = {
            "data": {
                # "user": user_id,
                "response": "yes"
            },
            "url": "/api/v1/meetups/{}/rsvps".format(meetup_id)
        }
        result = self.create_rsvp(url=rsvp_data.get(
            "url"), data=rsvp_data.get("data"), headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))
        db.tear_down()

    def test_missing_response_in_rsvp(self):
        """Tests if response is not given in rsvp"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        meetup = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data")[0].get("id")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        user = self.post_data(url=url, data=data, headers=headers)
        user_id = user.get("data")[0].get("id")
        self.assertEqual(status.created, user.get("status"))
        rsvp_data = {
            "data": {
                "user": user_id,
                # "response": "yes"
            },
            "url": "/api/v1/meetups/{}/rsvps".format(meetup_id)
        }
        result = self.create_rsvp(url=rsvp_data.get(
            "url"), data=rsvp_data.get("data"), headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))
        db.tear_down()
