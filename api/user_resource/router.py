from .controller import *
from api.base_resource.base import BaseResource
from common.models.user import User
from common.mongo import MongoWorker

from fastapi import FastAPI, APIRouter, Query, Depends


class UsersResource(BaseResource):

    def __init__(self, mongo: MongoWorker):
        super().__init__(mongo)
        self.router.add_api_route(
            "/user",
            self.get_users, # Обработчик
            methods=["GET"],
            # response_model=NoneType,
            # response_model_by_alias=True,
        )

    async def get_users(self, limit: int = Query(0, le=100), offset: int = Query(0, ge=0)):
        print(self.mongo.url)
        return None