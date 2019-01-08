from app.run import app


def client():
    client = app.test_client()
    return client
