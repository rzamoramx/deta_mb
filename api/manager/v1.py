
from fastapi import APIRouter, Response, status
import api.producer.request_models as rm
from api.producer.response_models import GenericResponse
from core.adm import make_topic, make_subscription

manager_v1 = APIRouter()


@manager_v1.post("/register_subs")
def register_subscription(subs: rm.SubscriptionModel, response: Response):
    if make_subscription(subs.name, subs.endpoint, subs.topic, subs.type_consuming):
        return GenericResponse(status="OK", detail="subscription created")
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse()


@manager_v1.post("/register_topic")
def register_topic(topic: rm.TopicModel, response: Response):
    if make_topic(topic.name):
        return GenericResponse(status="OK", detail="topic created")
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse()
