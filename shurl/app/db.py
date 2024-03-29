from datetime import datetime
from datetime import timedelta

from app import db_client
from app.exceptions import TokenAlreadyExistError
from app.exceptions import TokenNotFoundError


def is_token_exists(token):
    return db_client["tokens"].find_one({"token": token}) is not None


def add_token_to_db(token, original_url, expire_date=None):
    if is_token_exists(token):
        raise TokenAlreadyExistError(token)

    current_dttm = datetime.now()
    expire_date = (
        expire_date
        if expire_date
        else current_dttm + timedelta(days=30)
    )
    new_token_item = {
        "token": token,
        "url": original_url,
        "creation_dttm": current_dttm,
        "expire_dttm": expire_date,
    }
    new_stats_item = {
        "token": token,
        "clicks": 0,
    }
    db_client["tokens"].insert_one(document=new_token_item)
    db_client["stats"].insert_one(document=new_stats_item)


def update_stats(token: str):
    db_client["stats"].update_one(
        {"token": token}, {"$inc": {"clicks": 1}}
    )


def get_stats(token):
    if is_token_exists(token):
        return db_client["stats"].find_one({"token": token})["clicks"]
    else:
        raise TokenNotFoundError(token)
