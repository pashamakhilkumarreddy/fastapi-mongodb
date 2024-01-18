from bson import objectid
from fastapi import APIRouter, File, UploadFile, status

from ..helpers.save_picture import save_picture
from ..helpers.utils import get_response, raise_not_found_exception, result_verification
from ..models.user import User
from ..services import user_service as service

user_routes = APIRouter()

# base = "/api/v1/users"


@user_routes.post('/', status_code=status.HTTP_201_CREATED)
async def add_user(data: User):
    return await service.create_user(data)


@user_routes.get('/')
async def get_all():
    return await service.get_all_users()


@user_routes.get('/{id}')
async def get_by_id(id):
    return await result_verification(id)


@user_routes.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_user(id, data: User):
    await result_verification(id)
    done: bool = service.update_user(id, data)
    return get_response(done, error_message='An error occurred updating user information')


@user_routes.put('/image-upload/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def upload_user_image(id: str, file: UploadFile = File(...)):
    result = await result_verification(id)
    img, image_url = save_picture(file=file, folder_name='users', file_name=result['name'])
    done = await service.save_picture(id, [img, image_url])
    return get_response(done, error_message='An error occurred uploading user image')


@user_routes.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['users'])
async def delete_user(id):
    await result_verification(id)
    done: bool = await service.delete_user(id)
    return get_response(done, error_message='An error occurred deleting user')
