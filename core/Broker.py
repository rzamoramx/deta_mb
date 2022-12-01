
import uuid
import time
from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel
from persistance.detadb.DetaDB import DetaDB

db = DetaDB()


def process_message(msg: MessagePersistenceModel) -> str:
    msg.id = str(uuid.uuid4())
    msg.acked = False
    msg.ts_publisher_ack = round(time.time() * 1000)
    try:
        result = db.set_message(msg)
        if result is not None:
            return result['id']
    except Exception as e:
        print(f'Error occurred on process_message(): {e}')
    return None


def deliver_message(msg_id: str, msg: MessagePersistenceModel) -> bool:
    pass


def make_topic(topic_name: str) -> bool:
    topic = TopicPersistenceModel(topic_name)
    try:
        result = db.set_topic(topic, topic_name)
        print(f'result make_topic(): {result}')
        return True if result['ts'] > 0 else False
    except Exception as e:
        print(f'Error on make_topic(): {e}')
    return False


def make_subscription(sub_name: str, endpoint: str, topic: str) -> bool:
    subs = SubscriptionPersistenceModel(sub_name, topic, endpoint)
    try:
        result = db.set_subs(subs)
        print(f'result make_subscription(): {result}')
        return True if result['ts'] > 0 else False
    except Exception as e:
        print(f'Error on make_subscription(): {e}')
    return False
