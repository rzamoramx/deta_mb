
from fastapi import APIRouter
from api.rest.MessageModel import MessageModel
from api.rest.ResponseModel import ResponseModel
from persistance.MessagePersistenceModel import MessagePersistenceModel
from core.Broker import process_message

router_v1 = APIRouter()


@router_v1.post("/send_message", status_code=201, response_model=ResponseModel)
def send_message(message: MessageModel):
    msg_model = MessagePersistenceModel()

    process_message(msg_model)
