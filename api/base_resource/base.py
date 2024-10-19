from common.models.user import User
from common.mongo import MongoWorker

from fastapi import APIRouter, Request
from fastapi.routing import APIRoute


class BaseResource:

    def __init__(self, mongo: MongoWorker):
        self.router = APIRouter()
        self.mongo: MongoWorker = mongo
        # self.permissions = []
        # self.require_auth = False
