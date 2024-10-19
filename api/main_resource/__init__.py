from fastapi import APIRouter
# from api.base_resource.base import BaseAPIRouter
from .resources import *


class MainRouter:

    def __init__(self, mongo: MongoWorker):
        self.router = APIRouter()
        self.router.include_router(UnauthResource(mongo).router, prefix="/main_unauth")
        self.router.include_router(AuthResource(mongo).router, prefix="/main_auth")
