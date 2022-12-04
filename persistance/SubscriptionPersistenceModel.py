
import time
import uuid


class SubscriptionPersistenceModel(object):
    id: str
    topic: str
    type_consuming: str  # "PULL" or "PUSH"
    ts: int
    name: str
    endpoint: str

    def __init__(self, name: str, topic: str, type_consuming: str, endpoint: str, subs_id: str = ""):
        if subs_id == "":
            self.id = str(uuid.uuid4())
        self.topic = topic
        self.type_consuming = type_consuming
        self.ts = round(time.time() * 1000)
        self.name = name
        self.endpoint = endpoint
