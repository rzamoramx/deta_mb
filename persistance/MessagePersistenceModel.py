

class MessagePersistenceModel:
    id: str
    topic: str
    payload: str
    ts_published: int  # the timestamp that publisher sent message
    ts_publisher_ack: int  # the timestamp that broker acked the message to publisher

    def __init__(self, topic: str, payload: str, ts_published: int, ts_publisher_ack: int = 0):
        self.topic = topic
        self.payload = payload
        self.ts_published = ts_published
        self.ts_publisher_ack = ts_publisher_ack
