from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from shurl.db import get_stats
from shurl.db import get_url_by_token
from shurl.db import update_stats
from shurl.exceptions import TokenAlreadyExistError
from shurl.exceptions import TokenNotFoundError
from shurl.models import UrlRequest
from shurl.token_generator import generate_token
import uvicorn


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
    try:
        token = generate_token(
            url=url_request.original_url,
            custom_alias=url_request.custom_alias,
        )
    except TokenAlreadyExistError:
        raise HTTPException(
            status_code=400,
            detail="Custom alias token already exists",
        )
    else:
        return {"token": token}


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
    try:
        return {token: get_stats(token)}
    except TokenNotFoundError:
        raise HTTPException(status_code=404, detail="Token not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
