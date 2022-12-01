
from pydantic import BaseModel


class SubscriptionModel(BaseModel):
    name: str
    endpoint: str
    topic: str


class TopicModel(BaseModel):
    name: str


class MessageModel(BaseModel):
    # id: Union[str, None] = None
    topic: str
    type_consuming: str
    payload: str
    # timestamp: Union[int, None] = None
    timestamp: int
