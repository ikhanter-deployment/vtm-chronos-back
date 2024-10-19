from .controller import *
from api.base_resource.base import BaseResource, BaseResponse, role_required
from common.models.user import User
from common.mongo import MongoWorker
from .schemas import *

from fastapi import FastAPI, APIRouter, Query, Depends, Request


class CharactersResource(BaseResource):

    def __init__(self, mongo: MongoWorker):
        self.require_auth = True
        self.permissions = ['user']
        super().__init__(self.require_auth, self.permissions, mongo)
        self.router.add_api_route(
            "/",
            self.get_user, # Обработчик
            methods=["GET"],
            # response_model=None,
            # response_model_by_alias=True,
        )

    async def get_user(self, req: Request):
        
        characters = await get_characters(self.mongo, req.state.user.character_ids)
        return BaseResponse(data=characters)
    
    
