from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
# from fastapi.exceptions import HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse

from api.user_resource import UsersRouter
from api.base_resource.base import BaseResponse
from api.characters_resource import CharactersRouter
from api.main_resource import MainRouter
# from api.middlewares.auth import AuthMiddleware
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

app.state.mongo = mongo

app.include_router(CharactersRouter(mongo).router)
app.include_router(UsersRouter(mongo).router)
app.include_router(MainRouter(mongo).router)

@app.exception_handler(StarletteHTTPException)
def raise_http_exception(req: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=BaseResponse(status=exc.status_code, data=exc.detail).model_dump())
