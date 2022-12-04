

class MessagePersistenceModel:
    id: str
    topic: str
    payload: str
    ts_published: int
    ts_publisher_ack: int
    ts_consumer_ack: int
    acked: bool

    def __init__(self, topic: str, payload: str, ts_published: int):
        self.topic = topic
        self.payload = payload
        self.ts_published = ts_published
