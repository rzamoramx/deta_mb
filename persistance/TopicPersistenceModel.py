
import time
import uuid


class TopicPersistenceModel(object):
    id: str
    topic: str
    ts: int

    def __init__(self, topic: str, topic_id: str = ""):
        if topic_id == "":
            self.id = str(uuid.uuid4())
        self.topic = topic
        self.ts = round(time.time() * 1000)
