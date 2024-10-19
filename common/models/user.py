from common.utils.utils import generate_object_id, get_current_time, generate_token

from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    id: str = Field(default_factory=generate_object_id, alias="_id")
    username: str
    password: str = Field(exclude=True)
    token: str = Field(default_factory=generate_token, exclude=True)
    roles: list[str] = Field(default=["user"])
    character_ids: list[str] = Field(default_factory=list)
    chronicle_ids: list[str] = Field(default_factory=list)
    created_at: str = Field(default_factory=get_current_time)
    updated_at: str = Field(default_factory=get_current_time)
