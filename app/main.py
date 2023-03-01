import os
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
import redis


from fastapi import FastAPI

app = FastAPI()

origins = ["https://lively-grass-0786dc103.2.azurestaticapps.net"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    client = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, db=0)
    result = client.set("foo", "bar")
    value = client.get("foo")
    return {"Hello": "World", "result": result, "value": value}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
