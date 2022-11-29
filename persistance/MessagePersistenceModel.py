

class MessagePersistenceModel:
    id: str
    topic: str
    type_consuming: str
    payload: str
    ts_published: int
    ts_publisher_ack: int
    ts_consumer_ack: int
    acked: bool

    def __init__(self, topic: str, type_consuming: str, payload: str, ts_published: int):
        self.topic = topic
        self.type_consuming = type_consuming
        self.payload = payload
        self.ts_published = ts_published
