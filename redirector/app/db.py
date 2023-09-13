from app import db_client
from app.exceptions import TokenNotFoundError


def get_url_by_token(token: str) -> str:
    url = db_client.get(token)
    if not url:
        raise TokenNotFoundError()
    return url
