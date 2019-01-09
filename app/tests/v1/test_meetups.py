from .import client, db, meetu_data, status
import unittest
import json


class TestMeetup(unittest.TestCase):
    """Testst the operations performed on meetup records"""

    def create_meetup(self, url, data, headers):
        """Used for creating a meetup"""
        data = json.dumps(data)
        result = client().post(url=url, data=data, headers=headers)
        return json.loads(result.get_data(as_text=True))

    def test_successful_meetup(self):
        """Tests for successful creation of a meetup"""
        data = meetu_data.get("data")
        headers = meetu_data.get("headers")
        url = meetu_data.get("url")
        result = self.create_meetup(url=url, data=data, headers=headers)
        self.assertEqual(status.created, result.get("status"))
