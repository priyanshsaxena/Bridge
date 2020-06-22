import unittest

from app.app import App


class AppTest(unittest.TestCase):

    def test_app_root(self):
        with App.test_client() as tc:
            response = tc.get('/')
            assert response.data == b'Hello World'
            assert response.status_code == 200
