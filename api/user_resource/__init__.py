from fastapi import APIRouter
from .resources import *


class UsersRouter:

    def __init__(self, mongo: MongoWorker):
        self.router = APIRouter()
        self.router.include_router(UsersResource(mongo).router, prefix="/user")
        self.router.include_router(LoginResource(mongo).router, prefix="/login")
        self.router.include_router(RegisterResource(mongo).router, prefix="/register")
