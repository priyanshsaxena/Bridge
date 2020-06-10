from app import app

with app.test_client() as tc:
    response = tc.get('/')
    assert response.data == b'Hello World'
    assert response.status_code == 200
