
import time
import uuid


class TopicPersistenceModel(object):
    id: str
    name: str
    ts: int
    can_produce: bool  # disable topic to receive messages, if sets as False
    can_consume: bool  # disable topic to consume messages, affects all subscriptions even if they are enabled
    key: str  # DetaDB field

    def __init__(self, name: str, id: str = ""):
        if id == "":
            self.id = str(uuid.uuid4())
        self.name = name
        self.ts = round(time.time() * 1000)
        self.can_produce = True
        self.can_consume = True

    @classmethod
    def from_db(cls, id: str, name: str, ts: int, can_produce: bool, can_consume: bool, key: str):
        instance = cls(name, id)
        instance.ts = ts
        instance.can_produce = can_produce
        instance.can_consume = can_consume
        instance.key = key
        return instance
