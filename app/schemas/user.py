def userEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': str(item['name']),
        'profession': str(item['description']),
        'phone': int(item['phone']),
        'image_url': str(item['image_url']),
        'created_at': item['created_at'],
        'updated_at': item['updated_at'],
        'is_active': bool(item['image_url']),
    }


def usersEntities(entities) -> list:
    return [userEntity(item) for item in entities]
