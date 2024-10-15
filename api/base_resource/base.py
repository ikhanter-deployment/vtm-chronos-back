from common.models.user import User
from common.mongo import MongoWorker

from fastapi import FastAPI, APIRouter, Query, Depends


class BaseResource:

    def __init__(self, mongo: MongoWorker):
        self.router = APIRouter()
        self.mongo: MongoWorker = mongo
