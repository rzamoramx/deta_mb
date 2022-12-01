
import deta
import uuid
from persistance.MessagePersistenceInterface import MessagePersistenceInterface
from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel
from config.configs import detadb_settings as db_conf
from deta import Deta


class DetaDB(MessagePersistenceInterface):
    db_msgs: deta.Base
    db_topics: deta.Base
    db_subs: deta.Base

    def __init__(self):
        deta_i = Deta(db_conf.API_KEY)
        self.db_msgs = deta_i.Base('deta_mb_msgs')
        self.db_topics = deta_i.Base('deta_mb_topics')
        self.db_subs = deta_i.Base('deta_mb_subs')

    def set_subs(self, sub: SubscriptionPersistenceModel) -> dict:
        if sub.id is None or sub.id == "":
            sub.id = str(uuid.uuid4())
        return self.db_subs.put(sub.__dict__, sub.id)

    def set_topic(self, entity: TopicPersistenceModel, key: str = "") -> dict:
        if key == "":
            key = str(uuid.uuid4())
        return self.db_topics.put(entity.__dict__, key)

    def set_message(self, msg: MessagePersistenceModel) -> dict:
        if msg.id == "" or msg.id is None:
            msg.id = str(uuid.uuid4())
        return self.db_msgs.put(msg.__dict__, msg.id)

    def get_unacked(self) -> list[MessagePersistenceModel]:
        pass
