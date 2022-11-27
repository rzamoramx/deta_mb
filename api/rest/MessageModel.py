
from typing import Union
from pydantic import BaseModel


class MessageModel(BaseModel):
    id: str
    # company_description: Union[str, None] = None
    topic: str
    type_consuming: str
    payload: str
    timestamp: int
