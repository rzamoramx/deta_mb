
from abc import ABC, abstractmethod
from persistance.MessagePersistenceModel import MessagePersistenceModel


class MessagePersistenceInterface(ABC):
    @abstractmethod
    def set(self, msg: MessagePersistenceModel) -> str:
        pass

    @abstractmethod
    def get_unacked(self) -> list[MessagePersistenceModel]:
        pass
