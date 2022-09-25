import json

import pytest


class TestAPI:
    @pytest.fixture(autouse=True, scope="class")
    def setup(self, monkeysession, db_session):
        monkeysession.setattr("shurl.db.db_client", db_session)

    def model_to_json(self, model):
        return json.loads(model.json())

    def test_create_token_without_alias(
        self, api_client, url_request
    ):
        data = self.model_to_json(url_request)
        response = api_client.post("/get_token", json=data)
        assert response.status_code == 200
        result = response.json()["token"]
        assert type(result) == str

    def test_create_token_with_alias(self, api_client, url_request):
        url_request.custom_alias = "test_alias"
        data = self.model_to_json(url_request)
        response = api_client.post("/get_token", json=data)

        assert response.status_code == 200
        result = response.json()["token"]
        assert result == "test_alias"

    def test_create_token_with_exists_alias(
        self, api_client, url_request, added_token_item
    ):
        url_request.custom_alias = added_token_item["token"]
        data = self.model_to_json(url_request)
        response = api_client.post("/get_token", json=data)
        assert response.status_code == 400
        assert (
            response.text
            == '{"detail":"Custom alias token already exists"}'
        )

    def test_redirect_with_exists_token(
        self, api_client, added_token_item
    ):
        token = added_token_item["token"]
        response = api_client.get(f"/{token}", allow_redirects=False)
        assert response.is_redirect
        assert response.headers["location"] == added_token_item["url"]

    def test_redirect_with_unexists_token(self, api_client):
        unexists_token = "12" * 10
        response = api_client.get(
            f"/{unexists_token}", allow_redirects=False
        )
        assert response.status_code == 404
        assert response.text == '{"detail":"Token not found"}'

    def test_get_token_stats_with_exists_token(
        self, api_client, added_token_item
    ):
        token = added_token_item["token"]
        response = api_client.get(f"/stats/{token}")
        assert response.status_code == 200
        assert response.text == f'{{"{token}":0}}'

        api_client.get(f"/{token}", allow_redirects=False)
        response = api_client.get(f"/stats/{token}")
        assert response.status_code == 200
        assert response.text == f'{{"{token}":1}}'

    def test_get_token_stats_with_unexists_token(self, api_client):
        unexists_token = "12" * 10
        response = api_client.get(f"/stats/{unexists_token}")
        assert response.status_code == 404
        assert response.text == '{"detail":"Token not found"}'
