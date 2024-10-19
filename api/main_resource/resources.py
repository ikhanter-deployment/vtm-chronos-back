from .controller import *
from api.base_resource.base import BaseResource
from common.models.user import User
from common.mongo import MongoWorker
from .schemas import *

from fastapi import FastAPI, APIRouter, Query, Depends


# def require_authentication(require_auth: bool = True):
#     def decorator(func):
#         func.require_auth = require_auth
#         return func
#     return decorator

class UnauthResource(BaseResource):

    # @require_authentication(require_auth=False)
    def __init__(self, mongo: MongoWorker):
        super().__init__(mongo)
        self.require_auth = False
        self.permissions = []
        self.router.add_api_route(
            "/",
            self.get_info, # Обработчик
            methods=["GET"],
            # response_model=NoneType,
            # response_model_by_alias=True,
        )
        self.router.routes

    async def get_info(self):
        return ["HELLO KINDRED"]
    

class AuthResource(BaseResource):

    # @require_authentication(require_auth=True)
    def __init__(self, mongo: MongoWorker):
        super().__init__(mongo)
        self.require_auth = True
        self.permissions = ["admin"]
        self.router.add_api_route(
            "/",
            self.get_info,
            methods=["GET"],
            # response_model=NoneType,
            # response_model_by_alias=True,
        )

    async def get_info(self):
        return ["HELLO AUTHORIZED KINDRED"]
