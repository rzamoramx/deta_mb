
import uvicorn
from fastapi import FastAPI
from api.rest.v1 import router_v1

app = FastAPI()

app.include_router(router_v1, prefix="/v1")


@app.get("/ping")
def ping():
    return "ok"


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8080)
