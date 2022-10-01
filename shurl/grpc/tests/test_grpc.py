import re

import pytest
from shurl.grpc.definitions.builds.service_pb2 import Url


@pytest.mark.parametrize(
    "url",
    [
        "https://medium.com/geekculture/go-for-data-engineering-a45b6f858a11",
        "https://medium.com/apache-airflow/airflows-magic-loop-ec424b05b629",
        "https://medium.com/@graip.ai/ocr-tools-benchmark-e12d981cde3f",
    ],
)
def test_reply(grpc_stub, url):
    pattern = re.compile("https://hideuri.com/[A-Za-z0-9]+")
    request = Url(url_address=url)
    response = grpc_stub.GetTinyUrl(request)
    assert re.match(pattern, response.url_address)
