from shurl import db_client
from datetime import datetime, timedelta
from shurl.exceptions import TokenNotFoundError, TokenAlreadyExistError


def is_token_exists(token):
    ers = db_client['tokens'].find_one({"token": token})
    print(ers)
    return db_client['tokens'].find_one({"token": token}) is not None


def add_token_to_db(token, original_url, expire_date=None):
    if is_token_exists(token):
        raise TokenAlreadyExistError(token)

    current_dttm = datetime.now()
    expire_date = expire_date if expire_date else current_dttm + timedelta(days=30)
    new_token_item = {
        'token': token,
        'url': original_url,
        'creation_dttm': current_dttm,
        'expire_dttm': expire_date,
    }
    new_stats_item = {
        'token': token,
        'clicks': 0,
    }
    db_client['tokens'].insert_one(document=new_token_item)
    db_client['stats'].insert_one(document=new_stats_item)


def get_url_by_token(token):
    url = db_client['tokens'].find_one({"token": token})
    if url:
        return url['url']
    else:
        raise TokenNotFoundError()


def update_stats(token):
    db_client['stats'].update_one(
        {"token": token},
        {
            '$inc': {
                'clicks': 1
            }
        }
    )


def get_stats(token):
    if is_token_exists(token):
        return db_client['stats'].find_one({"token": token})['clicks']
    else:
        raise TokenNotFoundError(token)
