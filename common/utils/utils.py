from bson import ObjectId


def generate_object_id() -> str:
    return str(ObjectId())
