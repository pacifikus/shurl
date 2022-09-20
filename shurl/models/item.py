from pydantic import BaseModel


class Item(BaseModel):
    value: int
