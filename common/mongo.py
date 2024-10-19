
from common.controllers.base import CollectionsMixin

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient


class MongoWorker(CollectionsMixin):
    client: AsyncIOMotorClient | MongoClient

    def __init__(self, url: str, sync: bool = False):
        self.url = url
        if sync:
            self.client = MongoClient(url)
        else:
            self.client = AsyncIOMotorClient(url)

    def disconnect(self):
        self.client.close()

