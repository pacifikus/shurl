import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from db import get_url_by_token, get_stats, update_stats
from models import UrlRequest
from token_generator import generate_token
from exceptions import TokenNotFoundError

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


@app.post(
    "/get_token",
    summary="Generate token by url",
)
def create_token(url_request: UrlRequest) -> str:
    token = generate_token(
        url=url_request.original_url,
        custom_alias=url_request.custom_alias,
    )
    return {'token': token}


@app.get(
    "/{token}",
    summary="Redirect by token",
    response_class=RedirectResponse,
)
def redirect(token):
    try:
        url = get_url_by_token(token)
    except TokenNotFoundError:
        raise HTTPException(status_code=404, detail="Token not found")
    else:
        update_stats(token)
        return RedirectResponse(url=url)


@app.get(
    "/stats/{token}",
    summary="Get clicks stats by token",
)
def get_token_stats(token):
    return {token: get_stats(token)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)