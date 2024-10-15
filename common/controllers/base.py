from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from common.settings import MONGO_DB

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from common.mongo import MongoWorker


class CollectionsMixin:
    client: AsyncIOMotorClient | MongoClient

    _users_coll_name = "users"

    @property
    def users_coll(self):
        return self.client[MONGO_DB][self._users_coll_name]

