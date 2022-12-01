
import time
from typing import Union
from pydantic import BaseModel, Field


class GenericResponse(BaseModel):
    status: Union[str, None] = Field(default="NOK")
    detail: Union[str, None] = Field(default="error, retry later")


class SendMsgResponseModel(BaseModel):
    id: Union[str, None] = Field(default="")
    timestamp: Union[int, None] = Field(default=round(time.time() * 1000))
    ack: bool
    detail: str
