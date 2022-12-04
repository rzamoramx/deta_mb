
import unittest
from main import app
from fastapi.testclient import TestClient


class ConsumerTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_pulling(self):
        resp = self.client.get("http://localhost:8080/consumer/v1/pull/test/97b81b67-8ac3-4b96-a62d-fdb091bd87ce")
        print(f"response: {resp}")
