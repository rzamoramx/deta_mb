
from abc import ABC, abstractmethod
from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel


class MessagePersistenceInterface(ABC):
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
    def get_unacked(self) -> list[MessagePersistenceModel]:
        pass
