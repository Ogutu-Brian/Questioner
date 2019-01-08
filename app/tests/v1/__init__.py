from app.run import app
import pytest

app.config['TESTING'] = True


def client():
    client = app.test_client()
    return client


valid_user_data = {
    "headers": {
        "Content-Type": "application/json"
    },
    "data": {
        
    }
}
