from main import app,startup_event
from fastapi.testclient import TestClient
from api.models.letter import Letter
from api.models.user_info import UserInfo
from api.models.enterprise_info import EnterpriseInfo
from api.db.db import connect_and_init_db
import pytest


client = TestClient(app)
test_letter_id=""


def test_create_letter():
    user_info = UserInfo(
        name="John",
        last_name="Doe",
        email="john.doe@example.com",
        contact="1234567890",
        experience="Lorem ipsum dolor sit amet",
        date_of_solicitation="2022-01-01"
    )
    enterprise_info = EnterpriseInfo(
        recipient="Jane Smith",
        position="Software Engineer",
        name="ABC Company",
        vacant="Backend Developer",
        information="This is a test letter"
    )
    response = client.post("/letter", json={
        "user_info": user_info.model_dump(),
        "enterprise_info": enterprise_info.model_dump()
    })
    assert response.status_code == 200
    assert response.json()["content"] is not None


def test_save_letter_db():
    with TestClient(app) as client:
        letter = Letter(content="Test letter content")
        response = client.post("/letter-db", json=letter.model_dump())
        assert response.status_code == 201
        assert response.json()["letter"]["content"] == letter.content

def test_get_letter():
    with TestClient(app) as client:
        response = client.get("/letter-db/663ab59977e33564b9383a73")
        assert response.status_code == 201
        assert response.json()["letter"]["content"] is not None

@pytest.fixture
def get_test_letter_id():
    with TestClient(app) as client:
        response = client.post("/letter-db", json={"content": "Test letter content"})
        test_letter_id = response.json()["id"]
        yield test_letter_id
        client.delete(f"/letter-db/{test_letter_id}")



def test_create_letter_invalid_enterprise_info():
    
    user_info = UserInfo(
        name="John",
        last_name="Doe",
        email="john.doe@example.com",
        contact="1234567890",
        experience="Lorem ipsum dolor sit amet",
        date_of_solicitation="2022-01-01"
    )
    enterprise_info = {
        "recipient":"Jane Smith",
        "position":"Software Engineer",
        "name":"",
        "vacant":"Backend Developer"
    }
    response = client.post("/letter", json={
        "user_info": user_info.model_dump(),
        "enterprise_info": enterprise_info
    })
    assert response.status_code == 422  # Unprocessable Entity

def test_save_letter_db_invalid_content():
    with TestClient(app) as client:
        letter = {"qr":""}  # invalid content
        response = client.post("/letter-db", json=letter)
        assert response.status_code == 422  # Unprocessable Entity

def test_get_letter_not_found():
    response = client.get("/letter-db/999")  # Non-existent letter ID
    assert response.status_code == 404  # Not Found

