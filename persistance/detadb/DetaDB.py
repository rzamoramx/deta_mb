
import deta
from persistance.MessagePersistenceInterface import MessagePersistenceInterface
from persistance.MessagePersistenceModel import MessagePersistenceModel
from config.configs import detadb_settings as db_conf
from deta import Deta


class DetaDB(MessagePersistenceInterface):
    db: deta.Base

    def __init__(self):
        deta_i = Deta(db_conf.API_KEY)
        self.db = deta_i.Base('deta_mb')

    def set(self, msg: MessagePersistenceModel) -> dict:
        return self.db.put(msg.__dict__, msg.id)

    def get_unacked(self) -> list[MessagePersistenceModel]:
        pass
