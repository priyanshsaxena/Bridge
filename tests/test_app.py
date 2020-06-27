from app.app import App


def test_app_root():
    with App.test_client() as tc:
        response = tc.get('/')
        assert response.data == b'Hello World'
        assert response.status_code == 200
