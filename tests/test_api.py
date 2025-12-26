import pytest
from fastapi.testclient import TestClient
from app.main import app

def test_predict_positive_sentiment():
    # The 'with' block keeps the model loaded for the duration of the test
    with TestClient(app) as client:
        payload = {"text": "I absolutely love using FastAPI for building APIs!"}
        response = client.post("/predict", json=payload)
        
        assert response.status_code == 200
        assert response.json()["sentiment"] == "POSITIVE"

def test_predict_negative_sentiment():
    with TestClient(app) as client:
        payload = {"text": "This is the worst experience I have ever had. Terrible."}
        response = client.post("/predict", json=payload)
        
        assert response.status_code == 200
        assert response.json()["sentiment"] == "NEGATIVE"

def test_predict_empty_text():

    with TestClient(app) as client:
        payload = {
            "text": "   "
        }
        response = client.post("/predict", json=payload)
        assert response.status_code == 422  # Unprocessable Entity due to validation error
