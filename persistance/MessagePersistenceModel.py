

class MessagePersistenceModel:
    id: str
    topic: str
    type_consuming: str
    payload: str
    timestamp: int
    acked: bool
