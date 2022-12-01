
import json
from fastapi import APIRouter, Request, Depends, Response, status
import api.rest.request_models as rm
from api.rest.response_models import SendMsgResponseModel, GenericResponse
from persistance.MessagePersistenceModel import MessagePersistenceModel
from core.Broker import process_message, make_topic, make_subscription, deliver_message
from api.protobuf.deta_mb_pb2 import Msg

router_v1 = APIRouter()


async def parse_body(request: Request):
    data: bytes = await request.body()
    return data


@router_v1.post("/register_subs")
def register_subscription(subs: rm.SubscriptionModel, response: Response):
    if make_subscription(subs.name, subs.endpoint, subs.topic):
        return GenericResponse(status="OK", detail="subscription created")
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse()


@router_v1.post("/register_topic")
def register_topic(topic: rm.TopicModel, response: Response):
    if make_topic(topic.name):
        return GenericResponse(status="OK", detail="topic created")
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse()


@router_v1.post("/send_message", status_code=201, response_model=SendMsgResponseModel)
async def send_message(response: Response, data: bytes = Depends(parse_body)):
    msg = Msg()
    msg.ParseFromString(data)
    persist_model = MessagePersistenceModel(msg.topic, msg.type_consuming, msg.payload, msg.timestamp)
    msg_id = process_message(persist_model)
    if msg_id is None:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return SendMsgResponseModel(id="", ack=False, detail="error, retry later")
    else:
        deliver_message(msg_id, persist_model)
        return SendMsgResponseModel(id=msg_id, ack=True, detail="published")


def get_message_model(json_dct: dict) -> rm.MessageModel:
    # return namedtuple('X', json_dct.keys())(*json_dct.values())
    msg = rm.MessageModel(
        topic=json_dct['topic'],
        type_consuming=json_dct['type_consuming'],
        payload=json_dct['payload'],
        timestamp=json_dct['timestamp'],
    )

    return msg
