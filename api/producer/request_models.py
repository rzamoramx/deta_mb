
from pydantic import BaseModel


class SubscriptionManageModel(BaseModel):
    name: str
    can_consume: bool


class TopicManageModel(BaseModel):
    topic: str
    can_produce: bool
    can_consume: bool


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
