
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

    def update_msg(self, msg: MessagePersistenceModel) -> bool:
        try:
            return True if self.db_msgs.update(msg.__dict__, msg.id) is None else False
        except Exception as e:
            print(f'DetaDB ERROR, detail: {e}')
            return False

    def get_subs_by_id(self, sub_id: str) -> dict:
        return self.db_subs.get(sub_id)

    def get_subs_by_ttc(self, topic_name: str, type_consuming: str) -> [dict]:
        result = self.db_subs.fetch([{'topic': topic_name}, {'type_consuming': type_consuming}], limit=10)
        if result.count > 0:
            return result.items
        else:
            return []

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

    def get_unacked_by_topic(self, topic: str) -> list[dict]:
        result = self.db_msgs.fetch([{'topic': topic}, {'acked': False}], limit=100)
        if result.count > 0:
            return result.items
        else:
            return []
