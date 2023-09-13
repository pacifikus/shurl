from datetime import datetime
import random
import string

from fastapi.testclient import TestClient
import mongomock
import pytest
from shurl.app.main import app
from shurl.models.url import UrlRequest


@pytest.fixture(scope="session")
def monkeysession(request):
    from _pytest.monkeypatch import MonkeyPatch

    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()


@pytest.fixture(scope="session", autouse=True)
def db_session():
    db = mongomock.MongoClient()
    fake_db_client = db["test_db"]
    return fake_db_client


@pytest.fixture(scope="function")
def new_token_item():
    base = string.ascii_letters
    token = "".join(random.choice(base) for i in range(7))
    new_token_item = {
        "token": token,
        "url": "https://fastapi.tiangolo.com/",
        "creation_dttm": datetime.now(),
        "expire_dttm": datetime(2022, 12, 12),
    }
    new_stats_item = {
        "token": token,
        "clicks": 0,
    }
    return new_token_item, new_stats_item


@pytest.fixture(scope="function")
def added_token_item(db_session, new_token_item):
    db_session["tokens"].insert_one(document=new_token_item[0])
    db_session["stats"].insert_one(document=new_token_item[1])
    return new_token_item[0]


@pytest.fixture(scope="function")
def url_request():
    base = string.ascii_letters
    url = "".join(random.choice(base) for i in range(7))
    return UrlRequest(
        original_url=f"http://{url}",
    )


@pytest.fixture(scope="module")
def api_client():
    client = TestClient(app)
    yield client
