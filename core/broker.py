
import uuid
import time
from persistance.MessagePersistenceModel import MessagePersistenceModel

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
    # TODO: change this logic, the messages deliver at subscription level not message level, so for pulling subs
    # check messages unacked for actual subscription
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
        try:
            push_msg(msg_bin, msg_pm, sub['endpoint'])
            # TODO: ack message for actual subscription if ok (so create model field and logic)
        except Exception as ex:
            print(ex)
    # TODO: ack message occurs at subscription level not at message level (so remove logic and fields in model)
    ack_message(msg_pm)
