from uuid import UUID

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from common.mongo import MongoWorker
from common.models.user import User
from typing import List
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, mongo: MongoWorker):
        super().__init__(app)
        self.mongo = mongo

    async def dispatch(self, request: Request, call_next):

        response = await call_next(request)
        if str(response.status_code).startswith('3'):
            return response
        try:
            if request.scope["endpoint"].__self__.require_auth:
                token = request.headers.get("Authorization")
                if not token:
                    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

                user = await self.authorize_user(
                    self.mongo,
                    request.scope["endpoint"].__self__.permissions,
                    token
                )
                request.state.user = user
        except HTTPException as e:
            return JSONResponse(e.detail, status_code=e.status_code)
        return response
    
    async def authorize_user(self, mongo: MongoWorker, permissions: list[str], token: str):
        try:
            UUID(token, version=4)
        except ValueError as e:
            raise HTTPException(status_code=400)
        user_obj = await mongo.users_coll.find_one({"token": token})
        if not user_obj:
            raise HTTPException(status_code=400)
        if not permissions:
            return user_obj
        if not any(perm in user_obj["roles"] for perm in permissions):
            raise HTTPException(status_code=403)
        return user_obj
        