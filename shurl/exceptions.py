class FeijoaError(Exception):
    """Common class for feijoa exceptions."""


class TokenNotFoundError(Exception):
    """Raises if the given token doesn't exist."""


class TokenAlreadyExistError(Exception):
    """Raises if the generated token already exist in the DB."""
