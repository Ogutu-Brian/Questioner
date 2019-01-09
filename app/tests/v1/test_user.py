import unittest
from .import client, user_data, status
import json
from .import db


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
        db.tear_down()
        self.assertEqual(status.created, result.get("status"))

    def test_missing_email(self):
        """Tets for data that does not contain an email"""
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "firstname": "Ogutu",
            "lastname": "Brian",
            "othername": "Okinyi",
            "phoneNumber": "0703812914",
            "username": "Brian",
            # "email": "codingbrian58@gmail.com",
            "password": "password"
        }
        result = self.sign_up(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_passworord(self):
        """tests for data that is missing password during creation of user"""
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "firstname": "Ogutu",
            "lastname": "Brian",
            "othername": "Okinyi",
            "phoneNumber": "0703812914",
            "username": "Brian",
            "email": "codingbrian58@gmail.com",
            # "password": "password"
        }
        result = self.sign_up(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_first_name(self):
        """Tests for data that lacks first name during creation of user"""
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            # "firstname": "Ogutu",
            "lastname": "Brian",
            "othername": "Okinyi",
            "phoneNumber": "0703812914",
            "username": "Brian",
            "email": "codingbrian58@gmail.com",
            "password": "password"
        }
        result = self.sign_up(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_last_name(self):
        """Tests for data that misses last name during sign up"""
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "firstname": "Ogutu",
            # "lastname": "Brian",
            "othername": "Okinyi",
            "phoneNumber": "0703812914",
            "username": "Brian",
            "email": "codingbrian58@gmail.com",
            "password": "password"
        }
        result = self.sign_up(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_phone_number(self):
        """Tests for data that misses phone number during creation of a user"""
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "firstname": "Ogutu",
            "lastname": "Brian",
            "othername": "Okinyi",
            # "phoneNumber": "0703812914",
            "username": "Brian",
            "email": "codingbrian58@gmail.com",
            "password": "password"
        }
        result = self.sign_up(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_user_name(self):
        """tests for data that misses username during creation of user"""
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "firstname": "Ogutu",
            "lastname": "Brian",
            "othername": "Okinyi",
            "phoneNumber": "0703812914",
            # "username": "Brian",
            "email": "codingbrian58@gmail.com",
            "password": "password"
        }
        result = self.sign_up(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_data_not_json(self):
        """tests for data that is not in json format"""
        data = {
            "firstname": "Ogutu",
            "lastname": "Brian",
            "othername": "Okinyi",
            "phoneNumber": "0703812914",
            "username": "Brian",
            "email": "codingbrian58@gmail.com",
            "password": "password"
        }
        result = self.sign_up(url=user_data.get(
            "sign_up_url"), data=data)
        db.tear_down()
        self.assertEqual(status.not_json, result.get("status"))
