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
