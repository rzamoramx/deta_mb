
from fastapi import APIRouter, Response, status
import api.producer.request_models as rm
from api.producer.response_models import GenericResponse
from core.adm import make_topic, make_subscription, manage_topic_enable_disable, manage_subscription_enable_disable
from persistance.exceptions import *

manager_v1 = APIRouter()


@manager_v1.post("/manage_subscription")
def manage_subscription(subscription: rm.SubscriptionManageModel, response: Response):
    try:
        manage_subscription_enable_disable(subscription.name, subscription.can_consume)
        return GenericResponse(status=True, detail="subscription updated")
    except SubscriptionNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return GenericResponse(detail="subscription not found")
    except CannotUpdateSubscription as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse(detail=str(e))
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse(detail=f"unexpected exception: {e}")


@manager_v1.post("/manage_topic")
def manage_topic(topic: rm.TopicManageModel, response: Response):
    try:
        manage_topic_enable_disable(topic.topic, topic.can_produce, topic.can_consume)
        return GenericResponse(status="OK", detail="topic updated")
    except TopicNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return GenericResponse(detail="topic not found")
    except CannotUpdateTopic as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse(detail=str(e))
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse(detail=f"unexpected exception: {e}")


@manager_v1.post("/register_subs")
def register_subscription(subs: rm.SubscriptionModel, response: Response):
    try:
        make_subscription(subs.name, subs.endpoint, subs.topic, subs.type_consuming)
        return GenericResponse(status="OK", detail="subscription created")
    except SubscriptionAlreadyExists as e:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return GenericResponse(detail=str(e))
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse(detail=f"unexpected exception: {e}")


@manager_v1.post("/register_topic")
def register_topic(topic: rm.TopicModel, response: Response):
    try:
        make_topic(topic.name)
        return GenericResponse(status="OK", detail="topic created")
    except TopicAlreadyExists as e:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return GenericResponse(detail=str(e))
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return GenericResponse(detail=f"unexpected exception: {e}")
