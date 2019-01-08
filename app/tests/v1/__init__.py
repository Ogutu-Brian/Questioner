from app.run import app
import pytest
from app.api.v1.views import db

app.config['TESTING'] = True


def client():
    client = app.test_client()
    return client


user_data = {
    "headers": {
        "Content-Type": "application/json"
    },
    "sign_up": {
        "firstname": "Ogutu",
        "lastname": "Brian",
        "othername": "Okinyi",
        "phoneNumber": "0703812914",
        "username": "Brian",
        "email": "codingbrian58@gmail.com",
        "password": "password"
    },
    "sign_up_url": "/api/v1/users/sign-up"
}
