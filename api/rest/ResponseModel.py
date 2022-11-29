
import time
from typing import Union
from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    id: Union[str, None] = Field(default="")
    timestamp: Union[int, None] = Field(default=round(time.time() * 1000))
    ack: bool
    detail: str
