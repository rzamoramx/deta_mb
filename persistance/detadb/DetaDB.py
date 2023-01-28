
import deta
import uuid
from persistance.MessagePersistenceInterface import MessagePersistenceInterface
from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel
from persistance.LogSubsPersistenceModel import LogSubsPersistenceModel
from config.configs import detadb_settings as db_conf
from deta import Deta
from persistance.exceptions import *


class DetaDB(MessagePersistenceInterface):
    db_msgs: deta.Base
    db_topics: deta.Base
    db_subs: deta.Base
    db_log_subs: deta.Base

    def __init__(self):
        deta_i = Deta(db_conf.API_KEY)
        self.db_msgs = deta_i.Base('deta_mb_msgs')
        self.db_topics = deta_i.Base('deta_mb_topics')
        self.db_subs = deta_i.Base('deta_mb_subs')
        self.db_log_subs = deta_i.Base('deta_mb_log_subs')

    def upd_log_subs_message(self, log_subs: LogSubsPersistenceModel):
        updates = {}
        for attr, val in log_subs.__dict__.items():
            updates[attr] = val

        try:
            self.db_log_subs.update(updates, log_subs.id)
        except Exception as e:
            raise CannotUpdateLogSubsMessage(f'Cannot update log subs message, detail: {e}')

    def get_log_subs_mgs_by_sub_id_topic(self, sub_id: str, topic_id: str) -> [dict]:
        result = self.db_log_subs.fetch([{"subscription_id": sub_id, "topic_id": topic_id}], limit=100)
        if result.count > 0:
            return result.items
        else:
            return []

    def set_log_subs_message(self, log_subs: LogSubsPersistenceModel):
        if log_subs.id is None or log_subs.id == "":
            log_subs.id = str(uuid.uuid4())

        try:
            self.db_log_subs.put(log_subs.__dict__, log_subs.id)
        except Exception as e:
            raise CannotSetLogSubsMessage(f'Cannot set log subs message, detail: {e}')

    def get_subscription(self, key: str) -> SubscriptionPersistenceModel:
        subs = self.db_subs.get(key)
        if subs is None:
            raise SubscriptionNotFound
        return SubscriptionPersistenceModel.from_db(**subs)

    def upd_subscription(self, key: str, subscription: SubscriptionPersistenceModel):
        updates = {}
        for attr, val in subscription.__dict__.items():
            updates[attr] = val

        try:
            self.db_subs.update(updates, key)
        except Exception as e:
            raise CannotUpdateSubscription(f'Cannot update subscription {key}, detail: {e}')

    def get_topic(self, key: str) -> TopicPersistenceModel:
        topic = self.db_topics.get(key)
        if topic is None:
            raise TopicNotFound
        return TopicPersistenceModel.from_db(**topic)

    def upd_topic(self, key: str, topic: TopicPersistenceModel):
        updates = {}
        for attr, val in topic.__dict__.items():
            updates[attr] = val

        try:
            self.db_topics.update(updates, key)
        except Exception as e:
            raise CannotUpdateTopic(f'Cannot update topic {key}, detail: {e}')

    def update_msg(self, msg: MessagePersistenceModel):
        try:
            self.db_msgs.update(msg.__dict__, msg.id)
        except Exception as e:
            raise CannotUpdMessage(f'Cannot update message {msg.id}, detail: {e}')

    def update_log_subs(self, log_subs: LogSubsPersistenceModel):
        try:
            self.db_log_subs.update(log_subs.__dict__, log_subs.id)
        except Exception as e:
            raise CannotUpdLogSubs(f'Cannot update log subs {log_subs.id}, detail: {e}')

    def get_subs_by_id(self, sub_id: str) -> dict:
        return self.db_subs.get(sub_id)

    def get_subs_by_ttc(self, topic_name: str, type_consuming: str) -> [dict]:
        result = self.db_subs.fetch([{'topic': topic_name}, {'type_consuming': type_consuming}, {'can_consume': True}],
                                    limit=10)
        if result.count > 0:
            return result.items
        else:
            return []

    def get_subs_by_topic(self, topic_name: str) -> [dict]:
        result = self.db_subs.fetch([{'topic': topic_name}, {'can_consume': True}], limit=10)
        if result.count > 0:
            return result.items
        else:
            return []

    def set_subs(self, sub: SubscriptionPersistenceModel):
        if sub.id is None or sub.id == "":
            sub.id = str(uuid.uuid4())

        try:
            self.db_subs.insert(sub.__dict__, sub.id)
        except Exception:
            raise SubscriptionAlreadyExists

    def set_topic(self, entity: TopicPersistenceModel, key: str = ""):
        if key == "":
            key = str(uuid.uuid4())

        try:
            self.db_topics.insert(entity.__dict__, key)
        except Exception:
            raise TopicAlreadyExists

    def set_message(self, msg: MessagePersistenceModel) -> dict:
        if msg.id == "" or msg.id is None:
            msg.id = str(uuid.uuid4())

        try:
            return self.db_msgs.put(msg.__dict__, msg.id)
        except Exception as e:
            raise CannotInsertMessage(msg=f'Cannot insert message, detail: {e}')
