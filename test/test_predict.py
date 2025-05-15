from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_client():
    response = client.post("/api/v1/predict", json={"text": "Free money now!"})
    assert response.status_code == 200
    assert response.json()["result"] in ["spam", "not spam"]