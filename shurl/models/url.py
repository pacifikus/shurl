from pydantic import BaseModel, Field
from typing import Union


class UrlRequest(BaseModel):
    original_url: str
    custom_alias: Union[str, None] = Field(
        default=None, title="Custom alias for the given url instead of the token", max_length=10
    )
