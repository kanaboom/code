from typing import Union

from fastapi import FastAPI
from router import itemRouter

app = FastAPI()
app.include_router(itemRouter.router)


@app.get("/")
def read_root():
    return "OK";

