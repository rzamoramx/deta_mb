
from abc import ABC, abstractmethod
from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel


class MessagePersistenceInterface(ABC):
    @abstractmethod
    def get_subscription(self, key: str) -> SubscriptionPersistenceModel:
        pass

    @abstractmethod
    def upd_subscription(self, key: str, subscription: SubscriptionPersistenceModel) -> dict:
        pass

    @abstractmethod
    def get_topic(self, key: str) -> TopicPersistenceModel:
        pass

    @abstractmethod
    def upd_topic(self, key: str, topic: TopicPersistenceModel) -> dict:
        pass

    @abstractmethod
    def update_msg(self, msg: MessagePersistenceModel) -> bool:
        pass

    @abstractmethod
    def get_subs_by_id(self, sub_id: str) -> dict:
        pass

    @abstractmethod
    def get_subs_by_ttc(self, topic_name: str, type_consuming: str) -> [dict]:
        pass

    @abstractmethod
    def set_subs(self, sub: SubscriptionPersistenceModel) -> dict:
        pass

    @abstractmethod
    def set_topic(self, topic: TopicPersistenceModel, key: str = "") -> dict:
        pass

    @abstractmethod
    def set_message(self, msg: MessagePersistenceModel) -> dict:
        pass

    @abstractmethod
    def get_unacked_by_topic(self, topic_id: str) -> list[dict]:
        pass
