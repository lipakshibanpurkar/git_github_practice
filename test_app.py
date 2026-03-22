from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_post():
    client = app.test_client()
    response = client.post("/", data={"name": "Saurabh"})
    assert b"Hello, Saurabh!" in response.data