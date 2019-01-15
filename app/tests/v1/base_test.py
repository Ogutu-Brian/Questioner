import unittest
from .import app, db


class BaseTest(unittest.TestCase):
    app.config["TESTING"] = True

    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    def tearDown(self):
        db.tear_down()
