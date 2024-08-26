from mailbox import Message
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List



app = FastAPI()


class Message(BaseModel):
    content: str


messages: List[Message] = []


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/message/new")
async def post_message(message: Message):
    return {"massage"}


@app.get("/message/get")
async def get_massage(message: Message):
    return {"message"}


