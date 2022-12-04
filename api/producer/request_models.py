
from pydantic import BaseModel


class SubscriptionModel(BaseModel):
    name: str
    endpoint: str
    topic: str
    type_consuming: str  # "PULL" or "PUSH"


class TopicModel(BaseModel):
    name: str


class MessageModel(BaseModel):
    # id: Union[str, None] = None
    topic: str
    payload: str
    # timestamp: Union[int, None] = None
    timestamp: int
