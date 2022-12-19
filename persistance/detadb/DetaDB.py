
import deta
import uuid
from persistance.MessagePersistenceInterface import MessagePersistenceInterface
from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel
from config.configs import detadb_settings as db_conf
from deta import Deta
from persistance.exceptions import *


class DetaDB(MessagePersistenceInterface):
    db_msgs: deta.Base
    db_topics: deta.Base
    db_subs: deta.Base

    def __init__(self):
        deta_i = Deta(db_conf.API_KEY)
        self.db_msgs = deta_i.Base('deta_mb_msgs')
        self.db_topics = deta_i.Base('deta_mb_topics')
        self.db_subs = deta_i.Base('deta_mb_subs')

    def get_subscription(self, key: str) -> SubscriptionPersistenceModel:
        subs = self.db_subs.get(key)
        if subs is None:
            raise SubscriptionNotFound
        return SubscriptionPersistenceModel.from_db(**subs)

    def upd_subscription(self, key: str, subscription: SubscriptionPersistenceModel) -> dict:
        updates = {}
        for attr, val in subscription.__dict__.items():
            updates[attr] = val

        try:
            return self.db_subs.update(updates, key)
        except Exception as e:
            raise CannotUpdateSubscription(f'Cannot update subscription {key}, detail: {e}')

    def get_topic(self, key: str) -> TopicPersistenceModel:
        topic = self.db_topics.get(key)
        if topic is None:
            raise TopicNotFound
        return TopicPersistenceModel.from_db(**topic)

    def upd_topic(self, key: str, topic: TopicPersistenceModel) -> dict:
        updates = {}
        for attr, val in topic.__dict__.items():
            updates[attr] = val

        try:
            return self.db_topics.update(updates, key)
        except Exception as e:
            raise CannotUpdateTopic(f'Cannot update topic {key}, detail: {e}')

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
        try:
            return self.db_subs.insert(sub.__dict__, sub.id)
        except Exception:
            raise SubscriptionAlreadyExists

    def set_topic(self, entity: TopicPersistenceModel, key: str = "") -> dict:
        if key == "":
            key = str(uuid.uuid4())
        try:
            return self.db_topics.insert(entity.__dict__, key)
        except Exception:
            raise TopicAlreadyExists

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
