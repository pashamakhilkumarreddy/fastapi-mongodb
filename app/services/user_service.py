from typing import Optional

from bson import ObjectId

from ..config.db import db
from ..models.user import User
from ..schemas.serialize_objects import serialize_dict, serialize_list


async def get_all_users(start: Optional[int] = 0, limit: Optional[int] = 10) -> list:
    try:
        return serialize_list(db.users.find())
    except Exception as e:
        print(f'Error in index, {e}')
        return {'success': False, 'status': 500, 'data': {}, 'statusMessages': ['Internal Server error']}


async def get_by_id(id) -> dict:
    return serialize_dict(db.users.find_one({'_id': ObjectId(id)}))


async def create_user(data: User) -> dict:
    result = db.users.insert_one(dict(data))
    return serialize_dict(db.users.find_one({'_id': ObjectId(result.inserted_id)}))


async def update_user(id, data: User) -> bool:
    db.users.find_one_and_update({'_id': ObjectId(id)}, {'_set': dict(data)})
    return True


async def save_picture(id, image_data: dict) -> bool:
    image, url = image_data
    db.users.find_one_and_update({'_id': ObjectId(id)}, {'$set': {'image': image, 'image_url': url}})
    return True


async def delete_user(id) -> bool:
    db.users.find_one_and_delete({'_id': ObjectId(id)})
    return True
