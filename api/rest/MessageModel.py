
from pydantic import BaseModel


class MessageModel(BaseModel):
    # id: Union[str, None] = None
    topic: str
    type_consuming: str
    payload: str
    # timestamp: Union[int, None] = None
    timestamp: int
