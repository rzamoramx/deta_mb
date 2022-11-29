
import json
from fastapi import APIRouter, Request, Depends
from api.rest.MessageModel import MessageModel
from api.rest.ResponseModel import ResponseModel
from persistance.MessagePersistenceModel import MessagePersistenceModel
from core.Broker import process_message, deliver_message
from api.protobuf.deta_mb_pb2 import Msg

router_v1 = APIRouter()


async def parse_body(request: Request):
    data: bytes = await request.body()
    return data


@router_v1.post("/send_message", status_code=201, response_model=ResponseModel)
async def send_message(data: bytes = Depends(parse_body)):
    msg = Msg()
    msg.ParseFromString(data)
    persist_model = MessagePersistenceModel(msg.topic, msg.type_consuming, msg.payload, msg.timestamp)
    msg_id = process_message(persist_model)
    if msg_id is None:
        return ResponseModel(id="", ack=False, detail="error retry later")
    else:
        deliver_message(msg_id, persist_model)
        return ResponseModel(id=msg_id, ack=True, detail="published")


def get_message_model(json_dct: dict) -> MessageModel:
    # return namedtuple('X', json_dct.keys())(*json_dct.values())
    msg = MessageModel(
        topic=json_dct['topic'],
        type_consuming=json_dct['type_consuming'],
        payload=json_dct['payload'],
        timestamp=json_dct['timestamp'],
    )

    return msg
