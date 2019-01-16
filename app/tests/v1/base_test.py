import unittest
from .import app, db


class BaseTest(unittest.TestCase):
    app.config["TESTING"] = True

    def setUp(self):
        """Set up of application test client"""
        self.app = app
        self.client = self.app.test_client

    def tearDown(self):
        """Clears my db data"""
        db.tear_down()
