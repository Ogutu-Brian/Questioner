import unittest
from .import client, user_data
import json


class TestUser(unittest.TestCase):
    """A class for testing user endpoints and operations"""

    def sign_up(self, url, data={}, headers={}):
        """
        user sign up method by test client
        """
        result = client().post(url, data=json.dumps(data), headers=headers)
        return json.loads(result.get_data(as_text=True))

    def login(self, url, data={}, headers={}):
        """A method for logging in by test client"""
        result = client().post(url, data=json.dumps(data), headers=headers)
        return json.loads(result.get_dta(as_text=True))

    def test_valid_sign_up(self):
        """tests for a valid user sign up given correct data"""
        headers = user_data.get("headers")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        result = self.sign_up(url=url, data=data, headers=headers)
        self.assertEqual("success",result.get("status"))