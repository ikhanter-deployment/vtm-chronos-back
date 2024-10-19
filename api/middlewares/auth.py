# from uuid import UUID

# from fastapi import FastAPI, Request, Response, HTTPException, status
# from fastapi.responses import JSONResponse
# from common.mongo import MongoWorker
# from common.models.user import User
# from typing import List
# from starlette.middleware.base import BaseHTTPMiddleware
# from api.base_resource.base import BaseResponse


# class AuthMiddleware(BaseHTTPMiddleware):
#     def __init__(self, app: FastAPI, mongo: MongoWorker):
#         super().__init__(app)
#         self.mongo = mongo

#     async def authorize_user(self, mongo: MongoWorker, token: str):
#         try:
#             UUID(token, version=4)
#         except ValueError as e:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
#         user_from_db = await mongo.users_coll.find_one({"token": token})
#         user_obj = User(**user_from_db)
#         return user_obj

#     async def dispatch(self, request: Request, call_next):
#         token = request.headers.get("Authorization")
#         user = None
#         try:
#             if token:
#                 user = await self.authorize_user(
#                     self.mongo,
#                     token
#                 )
#             request.state.user = user

#             response = await call_next(request)

#             if str(response.status_code).startswith('3') or not request.scope.get("endpoint"):
#                 return response
            
#             if not request.scope["endpoint"].__self__.require_auth:
#                 return response

#             if not user:
#                 raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
#             if request.scope["endpoint"].__self__.permissions and not \
#                 any(perm in user.roles for perm in request.scope["endpoint"].__self__.permissions):
#                 raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
#         except HTTPException as e:
#             return JSONResponse({"status": "ERR", "data": e.detail}, status_code=e.status_code)
    
#         return response

