import pytest
import shurl
from shurl.exceptions import TokenAlreadyExistError
from shurl.exceptions import TokenNotFoundError


class TestDB:
    @pytest.fixture(autouse=True, scope="class")
    def setup(self, monkeysession, db_session):
        monkeysession.setattr("shurl.db.db_client", db_session)

    def test_is_token_exists_with_valid_token(self, added_token_item):
        assert shurl.db.is_token_exists(
            token=added_token_item["token"]
        )

    @pytest.mark.parametrize("token", ["", None, "123123123123"])
    def test_is_token_exists_with_invalid_token(self, token):
        assert not shurl.db.is_token_exists(token=token)

    def test_add_token_to_db_with_exists_token(
        self, added_token_item
    ):
        with pytest.raises(TokenAlreadyExistError):
            shurl.db.add_token_to_db(
                token=added_token_item["token"],
                original_url=added_token_item["url"],
            )

    def test_add_token_to_db_with_unexists_token(
        self, new_token_item
    ):
        token = new_token_item[0]["token"]
        url = new_token_item[0]["url"]

        shurl.db.add_token_to_db(
            token=token,
            original_url=url,
        )
        assert (
            shurl.db.db_client["tokens"].find_one({"token": token})
            is not None
        )
        assert (
            shurl.db.db_client["stats"].find_one({"token": token})
            is not None
        )

    def test_get_url_by_token_with_exists_token(
        self, added_token_item
    ):
        result = shurl.db.get_url_by_token(
            token=added_token_item["token"],
        )
        assert result == added_token_item["url"]

    def test_get_url_by_token_with_unexists_token(
        self, new_token_item
    ):
        with pytest.raises(TokenNotFoundError):
            shurl.db.get_url_by_token(
                token=new_token_item[0]["token"],
            )

    def test_update_stats_with_exists_token(self, added_token_item):
        token = added_token_item["token"]
        old_stats = shurl.db.db_client["stats"].find_one(
            {"token": token}
        )["clicks"]
        shurl.db.update_stats(token=token)
        token_info = shurl.db.db_client["stats"].find_one(
            {"token": token}
        )["clicks"]
        assert token_info == old_stats + 1

    def test_get_stats_with_exists_token(self, added_token_item):
        token = added_token_item["token"]
        result = shurl.db.get_stats(token=token)
        assert result == 0

    def test_get_stats_with_unexists_token(self, new_token_item):
        token = new_token_item[0]["token"]
        with pytest.raises(TokenNotFoundError):
            shurl.db.get_stats(token=token)
