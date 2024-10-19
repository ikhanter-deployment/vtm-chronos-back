from common.models.user import UserAPIState
from common.mongo import MongoWorker

from uuid import UUID


from fastapi import APIRouter, Request, Depends
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRoute
from typing import Any
from pydantic import BaseModel, Field


class BaseResource:

    def __init__(self, require_auth, permissions, mongo: MongoWorker):
        self.mongo: MongoWorker = mongo
        self.router = APIRouter(
            dependencies=[Depends(role_required(require_auth, permissions))]
        )
        # self.mongo: MongoWorker = mongo
        # self.permissions = []
        # self.require_auth = False


class BaseResponse(BaseModel):
    status: int = 200
    data: Any



async def authorize_user(req: Request, token: str):
    try:
        UUID(token, version=4)
    except ValueError as e:
        raise HTTPException(status_code=401)
    user_from_db = await req.app.state.mongo.users_coll.find_one({"token": token})
    user_obj = None
    if user_from_db:
        user_obj = UserAPIState(**user_from_db)
    return user_obj


def get_token(req: Request):
    return req.headers.get('Authorization')

def get_mongo():
    return 


async def get_current_user(req: Request, token: str = Depends(get_token)):
    user = None
    if token:
        user = await authorize_user(
            req,
            token
        )
    req.state.user = user
    return user


def role_required(require_auth: bool, required_roles: list):
    def role_checker(current_user: UserAPIState = Depends(get_current_user)):
        if required_roles:
            if not current_user:
                raise HTTPException(status_code=401)
            if not any(role in required_roles for role in current_user.roles):
                raise HTTPException(status_code=403)
        return current_user
    
    def return_none():
        return None
    if require_auth:
        return role_checker
    return return_none
    
