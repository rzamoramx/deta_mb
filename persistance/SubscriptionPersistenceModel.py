
import time
import uuid


class SubscriptionPersistenceModel(object):
    id: str
    topic: str
    type_consuming: str  # "PULL" or "PUSH"
    ts: int
    name: str
    endpoint: str
    can_consume: bool  # disable from consuming
    key: str  # DetaDB field

    def __init__(self, name: str, topic: str, type_consuming: str, endpoint: str, id: str = ""):
        if id == "":
            self.id = str(uuid.uuid4())
        self.topic = topic
        self.type_consuming = type_consuming
        self.ts = round(time.time() * 1000)
        self.name = name
        self.endpoint = endpoint
        self.can_consume = True

    @classmethod
    def from_db(cls, id: str, topic: str, type_consuming: str, ts: int, name: str, endpoint: str, can_consume: bool, key: str):
        instance = cls(name, topic, type_consuming, endpoint, id)
        instance.ts = ts
        instance.can_consume = can_consume
        instance.key = key
        return instance
