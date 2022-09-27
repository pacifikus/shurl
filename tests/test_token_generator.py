import re

import pytest
from shurl.token_generator import generate


@pytest.mark.parametrize("n", list(range(1, 8)))
def test_generate(n):
    generated_token = generate(n)
    pattern = re.compile("[A-Za-z0-9]+")
    assert type(generated_token) is str
    assert len(generated_token) == n
    assert re.match(pattern, generated_token)


def test_generate_token():
    ...
