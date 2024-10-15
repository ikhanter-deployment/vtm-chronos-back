from contextlib import asynccontextmanager

from passlib.context import CryptContext
from fastapi import FastAPI

from api.user_resource.router import UsersResource
from common.mongo import MongoWorker
from common.settings import MONGO_URL


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

mongo = MongoWorker(MONGO_URL)

@asynccontextmanager
async def lifespan(app: FastAPI):

    mongo.connect()
    print(mongo.url)
    print("Connected to the MongoDB database!")
    yield

    mongo.disconnect()
    print("MongoDB connection closed.")

app = FastAPI(lifespan=lifespan)

# init resources
app.include_router(UsersResource(mongo).router, prefix="/users")
