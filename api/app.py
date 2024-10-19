from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.user_resource import UsersRouter
from api.user_resource.resources import UsersResource
from api.main_resource import MainRouter
from api.middlewares.auth import AuthMiddleware
from common.mongo import MongoWorker
from common.settings import MONGO_URL


mongo = MongoWorker(MONGO_URL)

@asynccontextmanager
async def lifespan(app: FastAPI):

    print(mongo.url)
    print(type(mongo.client))
    print("Connected to the MongoDB database!")
    yield

    mongo.disconnect()
    print("MongoDB connection closed.")

app = FastAPI(
    lifespan=lifespan,
)

app.add_middleware(AuthMiddleware, mongo=mongo)

# init resources
# app.include_router(UsersResource(mongo).router)
app.include_router(UsersRouter(mongo).router)
app.include_router(MainRouter(mongo).router)
