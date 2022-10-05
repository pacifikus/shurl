import grpc
from shurl.grpc.definitions.builds.service_pb2 import Url
from shurl.grpc.definitions.builds.service_pb2_grpc import (
    TestServiceStub,
)


def main():
    """
    Creates a TestServiceStub and demonstrate the interaction with grpc server.
    """
    with grpc.insecure_channel("localhost:3000") as channel:
        client = TestServiceStub(channel)

        short_url = client.GetTinyUrl(
            Url(
                url_address="https://alek-cora-glez.medium.com/"
                            "my-next-api-grpc-restful-5d888289acd",
            )
        )
        print(short_url.url_address)


if __name__ == "__main__":
    main()
