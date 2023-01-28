
from abc import ABC, abstractmethod
from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel
from persistance.LogSubsPersistenceModel import LogSubsPersistenceModel


class MessagePersistenceInterface(ABC):
    @abstractmethod
    def upd_log_subs_message(self, log_subs: LogSubsPersistenceModel):
        pass

    @abstractmethod
    def get_log_subs_mgs_by_sub_id_topic(self, sub_id: str, topic_id: str) -> [dict]:
        pass

    @abstractmethod
    def set_log_subs_message(self, log_subs: LogSubsPersistenceModel):
        pass

    @abstractmethod
    def get_subscription(self, key: str) -> SubscriptionPersistenceModel:
        pass

    @abstractmethod
    def upd_subscription(self, key: str, subscription: SubscriptionPersistenceModel):
        pass

    @abstractmethod
    def get_topic(self, key: str) -> TopicPersistenceModel:
        pass

    @abstractmethod
    def upd_topic(self, key: str, topic: TopicPersistenceModel):
        pass

    @abstractmethod
    def update_msg(self, msg: MessagePersistenceModel):
        pass

    @abstractmethod
    def update_log_subs(self, log_subs: LogSubsPersistenceModel):
        pass

    @abstractmethod
    def get_subs_by_id(self, sub_id: str) -> dict:
        pass

    @abstractmethod
    def get_subs_by_ttc(self, topic_name: str, type_consuming: str) -> [dict]:
        pass

    @abstractmethod
    def get_subs_by_topic(self, topic_name: str) -> [dict]:
        pass

    @abstractmethod
    def set_subs(self, sub: SubscriptionPersistenceModel):
        pass

    @abstractmethod
    def set_topic(self, topic: TopicPersistenceModel, key: str = ""):
        pass

    @abstractmethod
    def set_message(self, msg: MessagePersistenceModel) -> dict:
        pass
