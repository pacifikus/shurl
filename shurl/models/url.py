from typing import Union

from pydantic import BaseModel
from pydantic import Field


class UrlRequest(BaseModel):
    original_url: str
    custom_alias: Union[str, None] = Field(
        default=None,
        title="Custom alias for the given url instead of the token",
        max_length=10,
    )
