
import asyncio
from fastapi import APIRouter, Request, Depends, Response, status
from api.producer.response_models import SendMsgResponseModel
from persistance.MessagePersistenceModel import MessagePersistenceModel
from core.broker import process_message
from api.protobuf.deta_mb_pb2 import Msg

producer_v1 = APIRouter()


async def parse_body(request: Request):
    data: bytes = await request.body()
    return data


@producer_v1.post("/send_message", status_code=201, response_model=SendMsgResponseModel)
async def send_message(response: Response, data: bytes = Depends(parse_body)):
    msg = Msg()
    msg.ParseFromString(data)
    persist_model = MessagePersistenceModel(msg.topic, msg.payload, msg.timestamp)
    msg_id, results = process_message(persist_model)
    if msg_id == "":
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return SendMsgResponseModel(id="", ack=False, detail="error, retry later")
    else:
        return SendMsgResponseModel(id=msg_id, ack=True, detail="results: " + str(results))
