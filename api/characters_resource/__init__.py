from fastapi import APIRouter
from .resources import *


class CharactersRouter:

    def __init__(self, mongo: MongoWorker):
        self.router = APIRouter()
        self.router.include_router(CharactersResource(mongo).router, prefix="/characters")
