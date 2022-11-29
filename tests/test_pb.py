
import unittest
import requests
from api.protobuf.deta_mb_pb2 import Msg


class Pb(unittest.TestCase):
    def test_make_request(self):
        msg = Msg()
        msg.topic = 'AB'
        msg.type_consuming = 0
        msg.payload = "{foo}"
        msg.timestamp = 1234567890123
        message = msg.SerializeToString(msg)

        res = requests.post(url='http://localhost:8080/v1/send_message',
                            data=message,
                            headers={'Content-Type': 'application/octet-stream'})
        print(f'response: {res}')

    def test_generate_pb(self):
        msg = Msg()
        msg.topic = 'AB'
        msg.type_consuming = 0
        msg.payload = "{foo}"
        msg.timestamp = 1234567890123
        message = msg.SerializeToString(msg)
        print(message)
