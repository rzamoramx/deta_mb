
from persistance.MessagePersistenceModel import MessagePersistenceModel


class LogSubsPersistenceModel(object):
    id: str
    subscription_id: str
    topic_id: str
    ts_published: int
    ts_consumed: int
    acked: bool
    message: MessagePersistenceModel

    def __init__(self, subs_id: str, topic_id: str, message: MessagePersistenceModel):
        self.subscription_id = subs_id
        self.topic_id = topic_id
        self.message = message
        self.acked = False
        self.ts_published = message.ts_published
        self.ts_consumed = 0

