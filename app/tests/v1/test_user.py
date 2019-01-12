import unittest
from .import client, user_data, status
import json
from .import db


class TestUser(unittest.TestCase):
    """A class for testing user endpoints and operations"""

    def post_data(self, url, data={}, headers={}):
        """
        Posts data to various endpoints
        """
        result = client().post(url, data=json.dumps(data), headers=headers)
        return json.loads(result.get_data(as_text=True))

    def test_valid_sign_up(self):
        """tests for a valid user sign up given correct data"""
        db.tear_down()
        headers = user_data.get("headers")
        data = user_data.get("sign_up")
        url = user_data.get("sign_up_url")
        result = self.post_data(url=url, data=data, headers=headers)
        self.assertEqual(status.created, result.get("status"))

    def test_missing_email(self):
        """Tets for data that does not contain an email"""
        db.tear_down()
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
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_passworord(self):
        """tests for data that is missing password during creation of user"""
        db.tear_down()
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
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        db.tear_down()
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_first_name(self):
        """Tests for data that lacks first name during creation of user"""
        db.tear_down()
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
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_last_name(self):
        """Tests for data that misses last name during sign up"""
        db.tear_down()
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
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_phone_number(self):
        """Tests for data that misses phone number during creation of a user"""
        db.tear_down()
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
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_user_name(self):
        """tests for data that misses username during creation of user"""
        db.tear_down()
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
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_data_not_json(self):
        """tests for data that is not in json format"""
        db.tear_down()
        headers = {
            # "Content-Type": "application/json"
        }
        data = {
            "firstname": "Ogutu",
            "lastname": "Brian",
            "othername": "Okinyi",
            "phoneNumber": "0703812914",
            "username": "Brian",
            "email": "codingbrian58@gmail.com",
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.not_json, result.get("status"))

    def test_taken_username(self):
        """Tests if a given username is already taken by another user"""
        db.tear_down()
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
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.created, result.get("status"))
        data = {
            "firstname": "Ogutu",
            "lastname": "Brian",
            "othername": "Okinyi",
            "phoneNumber": "0703812914",
            "username": "Brian",
            "email": "test@gmail.com",
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_taken_email(self):
        """Tests for signup with an email that is already taken by another user"""
        db.tear_down()
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
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.created, result.get("status"))
        data = {
            "firstname": "Ogutu",
            "lastname": "Brian",
            "othername": "Okinyi",
            "phoneNumber": "0703812914",
            "username": "Ogutu",
            "email": "codingbrian58@gmail.com",
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)

    def test_successful_user_login(self):
        """Tests for a successful user log in into Questioner"""
        db.tear_down()
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
            "password": "password12#B"
        }
        user = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.created, user.get("status"))
        login_data = {
            "email": "codingbrian58@gmail.com",
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "log_in_url"), data=login_data, headers=headers)
        self.assertEqual(status.success, result.get("status"))
        login_data = {
            "username": "Brian",
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "log_in_url"), data=login_data, headers=headers)
        self.assertEqual(status.success, result.get("status"))

    def test_missing_log_in_username_and_email(self):
        """Tests log in without the provision of both username and email"""
        db.tear_down()
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
            "password": "password12#B"
        }
        user = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.created, user.get("status"))
        login_data = {
            # "email": "codingbrian58@gmail.com",
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "log_in_url"), data=login_data, headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_missing_login_password(self):
        """Tests for missing password during login"""
        db.tear_down()
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
            "password": "password12#B"
        }
        user = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.created, user.get("status"))
        login_data = {
            "email": "codingbrian58@gmail.com",
            # "password": "password"
        }
        result = self.post_data(url=user_data.get(
            "log_in_url"), data=login_data, headers=headers)
        self.assertEqual(status.invalid_data, result.get("status"))

    def test_wrong_login_password(self):
        """Tests for invalid password during login"""
        db.tear_down()
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
            "password": "password12#B"
        }
        user = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.created, user.get("status"))
        login_data = {
            "email": "codingbrian58@gmail.com",
            "password": "password12#B4"
        }
        result = self.post_data(url=user_data.get(
            "log_in_url"), data=login_data, headers=headers)
        self.assertEqual(status.denied_access, result.get("status"))

    def test_unexisting_username(self):
        """Tests attempt to log in with unexisting username"""
        db.tear_down()
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
            "password": "password12#B"
        }
        user = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.created, user.get("status"))
        login_data = {
            "username": "HenkDebruin",
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "log_in_url"), data=login_data, headers=headers)
        self.assertEqual(status.denied_access, result.get("status"))

    def test_unexisting_email(self):
        """Tests for attempt to log in with unexisting email"""
        db.tear_down()
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
            "password": "password12#B"
        }
        user = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.created, user.get("status"))
        login_data = {
            "email": "testmail.@gmail.com",
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "log_in_url"), data=login_data, headers=headers)
        self.assertEqual(status.denied_access, result.get("status"))

    def test_non_json_login_data(self):
        db.tear_down()
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
            "password": "password12#B"
        }
        user = self.post_data(url=user_data.get(
            "sign_up_url"), data=data, headers=headers)
        self.assertEqual(status.created, user.get("status"))
        login_data = {
            "email": "codingbrian58@gmail.com",
            "password": "password12#B"
        }
        result = self.post_data(url=user_data.get(
            "log_in_url"), data=login_data, headers={})
        self.assertEqual(status.not_json, result.get("status"))
