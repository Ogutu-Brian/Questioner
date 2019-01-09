from app.run import app
import pytest
from app.api.v1.views import db, status

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
meetup_data = {
    "headers": {
        "Content-Type": "application/json"
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
question_data = {
    "headers": {
        "Content-Type": "application/json"
    },
    "data": {
        "title": "Responnsive Web design",
        "createdBy": 0,
        "response": "yes",
        "body": "What is the best way of getting around responsiveness of a website",
        "meetup": 0
    },
    "url": "/api/v1/questions"
}
