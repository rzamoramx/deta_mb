
import time
import requests
from api.protobuf.deta_mb_pb2 import Msg, RespPulling
from core.utils import retry_with_params
import core.broker
from fastapi import APIRouter, Response

consumer_v1 = APIRouter()


class OctetStreamResponse(Response):
    media_type = "application/octet-stream"


@consumer_v1.get("/pull/{topic}/{subscription_id}",
                 response_class=Response,
                 responses={
                     # Manually specify a possible response with our custom media type.
                     200: {
                         "content": {"application/octet-stream": {}}
                     }
                 })
def pull_msg(topic: str, subscription_id: str):
    resp_pulling = RespPulling()
    for msg in core.broker.deliver_msgs_for_pulling(topic, subscription_id):
        msg_proto = Msg()
        msg_proto.topic = msg.topic
        msg_proto.payload = msg.payload
        msg_proto.timestamp = round(time.time() * 1000)
        resp_pulling.messages.append(msg_proto)

    resp_pulling_bin = resp_pulling.SerializeToString()
    return Response(
        resp_pulling_bin,
        media_type="application/octet-stream",
    )


@retry_with_params(3)
def push_msg(msg_bin, url: str):
    res = requests.post(url=url,
                        data=msg_bin,
                        headers={'Content-Type': 'application/octet-stream'})
    if 200 <= res.status_code < 300:
        print(f'FAILED to deliver message: {res}')
    else:
        raise Exception(f"ERROR cannot deliver message after retries, response code from client: {res}")

    print(f'LOG: response from client: {res.content}')
