
from common.mongo import MongoWorker
from common.models.user import User
from common.settings import SECRET_KEY
from common.utils.pw_utils import get_password_hash, verify_password
from .schemas import *

from fastapi.exceptions import HTTPException


async def get_characters(mongo: MongoWorker, character_ids: list[str]):
    characters = await mongo.characters_coll.find(
        {"_id": {"$in": character_ids}}
    ).to_list(None)
    return characters
