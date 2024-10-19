from .controller import *
from api.base_resource.base import BaseResource
from common.models.user import User
from common.mongo import MongoWorker
from .schemas import *
from typing import Callable

from fastapi import Request, FastAPI, APIRouter, Query, Depends


class UnauthResource(BaseResource):

    def __init__(self, mongo: MongoWorker):
        self.require_auth = False
        self.permissions = []
        super().__init__(self.require_auth, self.permissions, mongo)
        self.router.add_api_route(
            "/",
            self.get_info, # Обработчик
            methods=["GET"],
            # response_model=NoneType,
            # response_model_by_alias=True,
        )

    async def get_info(self, req: Request):
        # print(req.state.user)
        return ["HELLO KINDRED"]
    

class AuthResource(BaseResource):

    def __init__(self, mongo: MongoWorker):
        self.require_auth = True
        self.permissions = ["user"]
        super().__init__(self.require_auth, self.permissions, mongo)
        self.router.add_api_route(
            "/",
            self.get_info,
            methods=["GET"],
            # response_model=NoneType,
            # response_model_by_alias=True,
        )

    async def get_info(self, req: Request):
        # print(req.state.user)
        return ["HELLO AUTHORIZED KINDRED"]
