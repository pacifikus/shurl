import json
import random

from locust import between
from locust import HttpUser
from locust import task


class LoadTestUser(HttpUser):
    wait_time = between(0.5, 2)

    def on_start(self):
        self.tokens = []
        self.create_token()  # To prevent cold start

    @task(2)
    def create_token(self):
        data = {"original_url": "https://www.google.com"}
        token = self.client.post(
            "get_token", data=json.dumps(data)
        ).json()
        self.tokens.append(token["token"])

    @task(20)
    def redirect(self):
        if self.tokens:
            token = random.choice(self.tokens)
        else:
            token = "test"
        self.client.get(f"{token}")

    @task(1)
    def get_stats(self):
        if self.tokens:
            token = random.choice(self.tokens)
        else:
            token = "test"
        self.client.get(f"stats/{token}")
