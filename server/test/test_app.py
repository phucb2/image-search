import unittest

from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)


class TestApp(unittest.TestCase):

    def test_read_item(self):
        response = client.get("/items/foo", headers={"X-Token": "fifafo"})
        assert response.status_code == 200
        assert response.json() == {"id": "foo", "title": "Foo", "description": "There goes my here"}

