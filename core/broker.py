
import uuid
import time
from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel
from persistance.detadb.DetaDB import DetaDB
from api.consumer.v1 import push_msg
from core.utils import retry_with_params
from api.protobuf.deta_mb_pb2 import Msg

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
    return ""


def deliver_msgs_for_pulling(topic: str, sub_id: str) -> [MessagePersistenceModel]:
    sub = db.get_subs_by_id(sub_id)
    if sub is None:
        raise Exception(f"subscription not found: {sub_id}, register it before")

    if sub['topic'] != topic:
        raise Exception(f"this subscription: {sub}, isn't registered to topic: {topic}")

    list_msgs = []
    for msg in db.get_unacked_by_topic(topic):
        msg_pm = MessagePersistenceModel(msg['topic'], msg['payload'], msg['ts_published'])
        msg_pm.acked = False
        msg_pm.ts_consumer_ack = round(time.time() * 1000)
        msg_pm.id = msg['id']
        list_msgs.append(msg_pm)
    return list_msgs


@retry_with_params(2)
def ack_message(msg: MessagePersistenceModel):
    msg.acked = True
    if not db.update_msg(msg):
        raise Exception(f"error during update, retrying, msg.id: {msg.id}")


async def deliver_mgs_for_push(msg_pm: MessagePersistenceModel):
    msg_proto = Msg()
    msg_proto.topic = msg_pm.topic
    msg_proto.payload = msg_pm.payload
    msg_proto.timestamp = round(time.time() * 1000)
    msg_bin = msg_proto.SerializeToString(msg_proto)

    subs = db.get_subs_by_ttc(msg_pm.topic, "PUSH")
    for sub in subs:
        push_msg(msg_bin, msg_pm, sub['endpoint'])
    # ack message
    ack_message(msg_pm)


def make_topic(topic_name: str) -> bool:
    topic = TopicPersistenceModel(topic_name)
    try:
        result = db.set_topic(topic, topic_name)
        print(f'result make_topic(): {result}')
        return True if result['ts'] > 0 else False
    except Exception as e:
        print(f'Error on make_topic(): {e}')
    return False


def make_subscription(sub_name: str, endpoint: str, topic: str, type_consuming: str) -> bool:
    subs = SubscriptionPersistenceModel(sub_name, topic, type_consuming, endpoint)
    try:
        result = db.set_subs(subs)
        print(f'result make_subscription(): {result}')
        return True if result['ts'] > 0 else False
    except Exception as e:
        print(f'Error on make_subscription(): {e}')
    return False
