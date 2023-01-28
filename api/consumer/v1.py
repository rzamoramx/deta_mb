
import time
import requests

from core.utils import retry_with_params
import core.broker
from fastapi import APIRouter, Response, status

consumer_v1 = APIRouter()


class OctetStreamResponse(Response):
    media_type = "application/octet-stream"


@consumer_v1.post("/pull/ack/{topic}/{subscription_id}")
def ack_message_for_subscription(topic: str, subscription_id: str):
    pass


@consumer_v1.get("/pull/{topic}/{subscription_id}",
                 response_class=Response,
                 responses={
                     200: {
                         "content": {"application/octet-stream": {}}
                     }
                 })
def pull_msg(topic: str, subscription_id: str):
    resp_pulling = core.broker.deliver_msgs_for_pulling(topic, subscription_id)
    resp_pulling_bin = resp_pulling.SerializeToString()

    return Response(
        resp_pulling_bin,
        media_type="application/octet-stream",
    )


@retry_with_params(2)
def push_msg(msg_bin, url: str):
    res = requests.post(url=url,
                        data=msg_bin,
                        headers={'Content-Type': 'application/octet-stream'})

    return res.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED, status.HTTP_204_NO_CONTENT]
