from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_schedule_announcement():
    response = client.post("/schedule_announcement", json={
        "id": 1,
        "content": "Hello, World!",
        "scheduled_time": "2024-05-01T12:00:00"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Announcement scheduled"}

def test_send_announcements():
    response = client.get("/send_announcements")
    assert response.status_code == 200
    assert response.json() == {"message": "Announcements sent"}

def test_scheduled_announcements():
    response = client.get("/scheduled_announcements")
    assert response.status_code == 200
    assert "scheduled_announcements" in response.json()
