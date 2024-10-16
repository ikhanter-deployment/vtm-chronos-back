import os

from dotenv import load_dotenv


load_dotenv("./config/.env")

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")
SECRET_KEY = os.getenv("SECRET_KEY")
