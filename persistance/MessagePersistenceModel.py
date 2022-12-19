

class MessagePersistenceModel:
    id: str
    topic: str
    payload: str
    ts_published: int  # the timestamp that publisher sent message
    ts_publisher_ack: int  # the timestamp that broker acked the message to publisher
    acked: bool  # the confirmation (ack) of broker

    def __init__(self, topic: str, payload: str, ts_published: int):
        self.topic = topic
        self.payload = payload
        self.ts_published = ts_published
        self.ts_publisher_ack = 0
        self.acked = False
