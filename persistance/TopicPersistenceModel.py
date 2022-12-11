
import time
import uuid


class TopicPersistenceModel(object):
    id: str
    topic: str
    ts: int
    can_produce: bool  # disable topic to receive messages, if sets as False
    can_consume: bool  # disable topic to consume messages, affects all subscriptions even if they are enabled (can_consume = True)
    subs_can_consume: [str]  # to avoid extra queries, list of subs can consume, this field must be updated always

    def __init__(self, topic: str, topic_id: str = ""):
        if topic_id == "":
            self.id = str(uuid.uuid4())
        self.topic = topic
        self.ts = round(time.time() * 1000)
        self.can_produce = True
        self.can_consume = True
        self.subs_can_consume = []
