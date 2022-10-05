from concurrent.futures import ThreadPoolExecutor
import json

from definitions.builds.service_pb2 import Url
from definitions.builds.service_pb2_grpc import (
    add_TestServiceServicer_to_server,
)
from definitions.builds.service_pb2_grpc import TestServiceServicer
import grpc
import requests


class Service(TestServiceServicer):
    def GetTinyUrl(self, request: Url, context):
        """
        Takes an url as input and returns the shortened version of that URL.

        :param self: Access the class attributes and methods
        :param request:Url: Long url to pass through hideuri.com url shortener
        :param context: Control the lifetime of rpc calls
        :return: An Url object with generated short url
        :doc-author: Trelent
        """
        result = requests.post(
            url="https://hideuri.com/api/v1/shorten",
            data={"url": request.url_address},
        )
        url_address = json.loads(result.text)["result_url"]
        return Url(url_address=url_address)


def execute_server():
    """
    Creates a gRPC server and listens on port 3000 until termination.
    """
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
