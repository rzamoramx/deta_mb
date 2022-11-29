
import uuid
import time
from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.detadb.DetaDB import DetaDB

db = DetaDB()


def process_message(msg: MessagePersistenceModel) -> str:
    msg.id = str(uuid.uuid4())
    msg.acked = False
    msg.ts_publisher_ack = round(time.time() * 1000)
    try:
        result = db.set(msg)
        if result is not None:
            return result['id']
    except Exception as e:
        print(f'error occurred on persist: {e}')
    return None


def deliver_message(msg_id: str, msg: MessagePersistenceModel) -> bool:
    pass
