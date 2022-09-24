import string
import random
from db import is_token_exists, add_token_to_db
from exceptions import TokenAlreadyExistError


symbols = string.ascii_letters + string.digits


def generate(n=7):
    return ''.join(random.choices(symbols, k=n))


def generate_token(url, custom_alias):
    if custom_alias:
        if is_token_exists(custom_alias):
            raise TokenAlreadyExistError(custom_alias)
        else:
            add_token_to_db(token=custom_alias, original_url=url)
    else:
        while True:
            generated = generate()
            try:
                add_token_to_db(token=generated, original_url=url)
                return generated
            except TokenAlreadyExistError:
                print('Trying another generation...') # TODO: logging
