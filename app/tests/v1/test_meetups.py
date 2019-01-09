from .import client, db, meetup_data, status
import unittest
import json


class TestMeetup(unittest.TestCase):
    """Testst the operations performed on meetup records"""

    def create_meetup(self, url="", data={}, headers={}):
        """Used for creating a meetup"""
        data = json.dumps(data)
        result = client().post(url, data=data, headers=headers)
        return json.loads(result.get_data(as_text=True))

    def test_successful_meetup(self):
        """Tests for successful creation of a meetup"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        result = self.create_meetup(url=url, data=data, headers=headers)
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
        result = self.create_meetup(url=url, data=data, headers=headers)
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
        result = self.create_meetup(url=url, data=data, headers=headers)
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
        result = self.create_meetup(url=url, data=data, headers=headers)
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
        result = self.create_meetup(url=url, data=data, headers=headers)
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
        result = self.create_meetup(url=url, data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.not_json, result.get("status"))

    def test_get_meetup_record(self):
        """Tests for get request for a specific meetup given a meetup id"""
        data = meetup_data.get("data")
        headers = meetup_data.get("headers")
        url = meetup_data.get("url")
        meetup = self.create_meetup(url=url, data=data, headers=headers)
        self.assertEqual(status.created, meetup.get("status"))
        meetup_id = meetup.get("data").get("id")
        get_url = "/api/v1/{}".format(meetup_id)
        result = json.loads(client().get(get_url).get_data(as_text=True))
        db.tear_down()
