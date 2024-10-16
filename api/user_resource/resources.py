from .controller import *
from api.base_resource.base import BaseResource
from common.models.user import User
from common.mongo import MongoWorker
from .schemas import *

from fastapi import FastAPI, APIRouter, Query, Depends


class UsersResource(BaseResource):

    def __init__(self, mongo: MongoWorker):
        super().__init__(mongo)
        self.router.add_api_route(
            "/",
            self.get_users, # Обработчик
            methods=["GET"],
            # response_model=NoneType,
            # response_model_by_alias=True,
        )

    async def get_users(self, limit: int = Query(0, le=100), offset: int = Query(0, ge=0)):
        print(self.mongo.url)
        return None
    

class RegisterResource(BaseResource):

    def __init__(self, mongo: MongoWorker):
        super().__init__(mongo)
        self.router.add_api_route(
            "/",
            self.post_registration,
            methods=["POST"],
            # response_model=NoneType,
            # response_model_by_alias=True,
        )

    async def post_registration(self, body: AuthSchema):
        if await is_existing_username(self.mongo, body.username):
            raise HTTPException(422, "Username already exists")
        token = await register_user(self.mongo, body)
        return {
            "token": token
        }
    

class LoginResource(BaseResource):

    def __init__(self, mongo: MongoWorker):
        super().__init__(mongo)
        self.router.add_api_route(
            "/",
            self.post_login,
            methods=["POST"],
            # response_model=NoneType,
            # response_model_by_alias=True,
        )

    async def post_login(self, body: AuthSchema):
        try:
            token = await get_user_token(self.mongo, body)
        except TypeError as e:
            raise HTTPException(422, e.__str__())
        return {
            "token": token
        }