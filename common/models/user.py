from common.utils.utils import generate_object_id

from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(default_factory=generate_object_id, alias="_id")
    username: str
    password: str
    character_ids: list[str] = Field(default_factory=list)
    chronicle_ids: list[str] = Field(default_factory=list)
