import uuid

from bson import ObjectId
from datetime import datetime

import pytz


def generate_object_id() -> str:
    return str(ObjectId())

def get_current_time() -> str:
    return datetime.now(pytz.utc).isoformat()

def generate_token() -> str:
    return uuid.uuid4().hex