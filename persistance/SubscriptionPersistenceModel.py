
import time
import uuid


class SubscriptionPersistenceModel(object):
    id: str
    topic: str
    ts: int
    name: str
    endpoint: str

    def __init__(self, name: str, topic: str, endpoint: str, subs_id: str = ""):
        if subs_id == "":
            self.id = str(uuid.uuid4())
        self.topic = topic
        self.ts = round(time.time() * 1000)
        self.name = name
        self.endpoint = endpoint
