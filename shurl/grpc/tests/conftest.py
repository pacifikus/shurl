import pytest
from shurl.grpc.definitions.builds.service_pb2_grpc import (
    add_TestServiceServicer_to_server,
)
from shurl.grpc.definitions.builds.service_pb2_grpc import (
    TestServiceStub,
)
from shurl.grpc.server import Service


@pytest.fixture(scope="module")
def grpc_add_to_server():
    return add_TestServiceServicer_to_server


@pytest.fixture(scope="module")
def grpc_servicer():
    return Service()


@pytest.fixture(scope="module")
def grpc_stub(grpc_channel):
    return TestServiceStub(grpc_channel)
