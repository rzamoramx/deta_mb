
import uuid
import time

from persistance.MessagePersistenceModel import MessagePersistenceModel
from persistance.LogSubsPersistenceModel import LogSubsPersistenceModel
from persistance.detadb.DetaDB import DetaDB
import persistance.exceptions as ex
from api.protobuf.deta_mb_pb2 import Msg, RespPulling

from api.consumer.v1 import push_msg
from core.utils import retry_with_params

db = DetaDB()


def process_message(msg: MessagePersistenceModel) -> (str, str):
    """
    process message (publisher), persist and deliver it to push subscribers
    :param msg: an instance of MessagePersistenceModel
    :return: tuple (id of message, array of results for each subscription)
    """
    results_subs = []
    msg.id = str(uuid.uuid4())
    msg.acked = False
    msg.ts_publisher_ack = round(time.time() * 1000)

    # backup message
    res = db.set_message(msg)

    # prepare message for delivery
    msg_proto = Msg()
    msg_proto.topic = msg.topic
    msg_proto.payload = msg.payload
    msg_proto.timestamp = round(time.time() * 1000)
    msg_bin = msg_proto.SerializeToString(msg_proto)

    # for each subscription
    subs = db.get_subs_by_topic(msg.topic)
    for sub in subs:
        log_subs_persistence = LogSubsPersistenceModel(sub['id'], msg.topic, msg)

        # persist a copy of message in log_subs_msg and try to deliver it, only for PUSH subs
        if sub['type_consuming'] == "PUSH":
            results_subs.append(atomic_deliver_msgs_for_push(msg_bin, sub, log_subs_persistence))

    return res['id'], results_subs


def atomic_deliver_msgs_for_push(msg_bin, sub: dict, log_subs_persistence: LogSubsPersistenceModel) -> str:
    db.set_log_subs_message(log_subs_persistence)

    if sub['type_consuming'] == "PUSH":
        try:
            res = push_msg(msg_bin, sub['endpoint'])
            if res:
                ack_message_for_subscription(log_subs_persistence, sub['id'])
        except Exception as e:
            return str(e)
    return ""


def ack_msgs_for_pulling(topic: str, sub_id: str, list_log_subs: [str]):
    validations(topic, sub_id)


def deliver_msgs_for_pulling(topic: str, sub_id: str) -> RespPulling:
    validations(topic, sub_id)

    resp_pulling = RespPulling()
    # get messages pending to deliver for actual subscription
    for msg in db.get_log_subs_mgs_by_sub_id_topic(sub_id, topic):
        msg_pm = MessagePersistenceModel(**msg['message'])
        msg_proto = Msg()
        msg_proto.topic = msg_pm.topic
        msg_proto.payload = msg_pm.payload
        msg_proto.timestamp = round(time.time() * 1000)
        msg_proto.log_subs_msg_id = msg['id']

        resp_pulling.messages.append(msg_proto)

    return resp_pulling


@retry_with_params(2)
def ack_message_for_subscription(msg: LogSubsPersistenceModel):
    """this method acknowledge message as a consumer, not a publisher"""
    msg.acked = True
    msg.ts_consumed = round(time.time() * 1000)
    db.update_log_subs(msg)


def validations(topic: str, sub_id: str):
    sub = db.get_subs_by_id(sub_id)
    if sub is None:
        raise ex.SubscriptionNotFound(f"subscription not found: {sub_id}, register it before")

    if sub['topic'] != topic:
        raise Exception(f"this subscription: {sub}, isn't registered to topic: {topic}")
