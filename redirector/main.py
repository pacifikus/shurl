import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from app.db import get_url_by_token
from app.exceptions import TokenNotFoundError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI(
    title="Shurl redirector",
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
    "/{token}",
    summary="Redirect by token",
    response_class=RedirectResponse,
)
def redirect(token):
    try:
        url = get_url_by_token(token)
        logger.info(f'Short url for {url} created')
    except TokenNotFoundError:
        raise HTTPException(status_code=404, detail="Token not found")
    else:
        return RedirectResponse(url=url)
