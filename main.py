
import uvicorn
from fastapi import FastAPI
from api.producer.v1 import router_v1
from api.consumer.v1 import consumer_v1

app = FastAPI()

app.include_router(router_v1, prefix="/producer/v1")
app.include_router(consumer_v1, prefix="/consumer/v1")


@app.get("/ping")
def ping():
    return "ok"


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8080)
