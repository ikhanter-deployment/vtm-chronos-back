
from common.mongo import MongoWorker
from common.models.user import User
from common.settings import SECRET_KEY
from common.utils.pw_utils import get_password_hash, verify_password
from .schemas import *

from fastapi.exceptions import HTTPException


async def is_existing_username(mongo: MongoWorker, username: str):
    if await mongo.users_coll.find_one({"username": username}):
        return True
    return False

async def register_user(mongo: MongoWorker, user_object: AuthSchema):
    user_object.password = get_password_hash(user_object.password)
    user = User(**user_object.model_dump()).model_dump(by_alias=True)
    await mongo.users_coll.insert_one(user)

    return user["token"]

async def get_user_token(mongo: MongoWorker, user_object: AuthSchema):
    user = await mongo.users_coll.find_one({"username": user_object.username})
    if not user:
        raise TypeError("Username doesn't exist")
    if not verify_password(user_object.password, user["password"]):
        raise TypeError("Password is not correct")
    return user["token"]