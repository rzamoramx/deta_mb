
import asyncio
from fastapi import APIRouter, Request, Depends, Response, status
import api.producer.request_models as rm
from api.producer.response_models import SendMsgResponseModel, GenericResponse
from persistance.MessagePersistenceModel import MessagePersistenceModel
from core.broker import process_message, make_topic, make_subscription, deliver_mgs_for_push
from api.protobuf.deta_mb_pb2 import Msg

router_v1 = APIRouter()


async def parse_body(request: Request):
    data: bytes = await request.body()
    return data


@router_v1.post("/register_subs")
def register_subscription(subs: rm.SubscriptionModel, response: Response):
    if make_subscription(subs.name, subs.endpoint, subs.topic, subs.type_consuming):
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
    persist_model = MessagePersistenceModel(msg.topic, msg.payload, msg.timestamp)
    msg_id = process_message(persist_model)
    if msg_id == "":
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return SendMsgResponseModel(id="", ack=False, detail="error, retry later")
    else:
        # try to deliver message
        asyncio.run(deliver_mgs_for_push(msg))
        return SendMsgResponseModel(id=msg_id, ack=True, detail="published")
