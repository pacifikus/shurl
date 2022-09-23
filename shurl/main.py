from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .models import Item


app = FastAPI(
    title="Shurl",
    description="Url shortener",
    version="0.0.1",
    contact={
        "name": "pacifikus",
        "email": "masterkristall@gmail.com",
    },
    docs_url="/docs",
    redoc_url=None,
)


@app.get(
    "/hello",
    summary="Path request",
)
def read_root():
    return {"Hello": "World"}


@app.get(
    "/items/{item_id}",
    summary="Query request",
)
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post(
    "/tostring",
    summary="Body request",
    response_class=HTMLResponse,
)
def to_string(body: Item) -> str:
    return str(body)
