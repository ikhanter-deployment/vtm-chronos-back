from common.models.user import User
from common.mongo import MongoWorker

from fastapi import APIRouter, Request
from fastapi.routing import APIRoute


class BaseResource:

    def __init__(self, mongo: MongoWorker):
        self.router = APIRouter()
        self.mongo: MongoWorker = mongo
        self.permissions = []
        self.require_auth = False


# class BaseAPIRouter(APIRouter):

#     def __init__(self, *args, require_auth: bool = False, permissions: list[str] = [], **kwargs):
#         super().__init__(*args, **kwargs)
#         self.require_auth = require_auth
#         self.permissions = permissions

#     def add_api_route(self, *args, **kwargs) -> None:
#         route = self.route_class(*args, **kwargs)
#         self.routes.append(route)


# class BaseAPIRoute(APIRoute):

#     def __init__(self, *args, require_auth: bool = False, permissions: list[str] = [], **kwargs):
#         if kwargs.get('route_class_override'):
#             del kwargs["route_class_override"]
#         super().__init__(*args, **kwargs)
#         self.require_auth = require_auth
#         self.permissions = permissions
