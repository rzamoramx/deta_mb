
import unittest
import requests
from api.rest.request_models import TopicModel


class Topic(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Topic, self).__init__(*args, **kwargs)

    def test_make_topic(self):
        topic = TopicModel(name="test")
        topic.name = "test"

        res = requests.post(url='http://localhost:8080/v1/register_topic',
                            json=topic.__dict__,
                            headers={'Content-Type': 'application/json'})
        print(f'response: {res}')
