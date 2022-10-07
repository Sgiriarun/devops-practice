from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "Message": "Welcome to ask_arun web app by using seach and list"
    }


def test_phrase():
    response = client.get("/phrase_it/arun kumar")
    assert response.status_code == 200
    assert response.json() == {
        "output": ["arun vijay", "november", "arun kumar", "indian actor", "tamil"]
    }
