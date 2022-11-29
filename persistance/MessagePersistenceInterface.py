
from abc import ABC, abstractmethod
from persistance.MessagePersistenceModel import MessagePersistenceModel


class MessagePersistenceInterface(ABC):
    @abstractmethod
    def set(self, msg: MessagePersistenceModel) -> dict:
        pass

    @abstractmethod
    def get_unacked(self) -> list[MessagePersistenceModel]:
        pass
