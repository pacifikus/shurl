import redis
import requests
import json


class TestSaveNewToken:
    def setup(self):
        self.shortener_url = 'http://localhost:5002'
        self.redirector_url = 'http://localhost:5002'
        self.redis_client = redis.Redis(
            host='localhost',
            port=6379,
            decode_responses=True
        )
        self.original_url = "https://www.youtube.com/watch?v=3X-TAuWdIAc&t=2857s"

    def test_create_token(self):
        response = requests.post(
            url=self.shortener_url + '/get_token',
            json={"original_url": self.original_url}
        )
        token = json.loads(response.text)['token']
        assert self.redis_client.get(token) == self.original_url
