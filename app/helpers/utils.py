from bson import objectid
from fastapi import HTTPException, status

from ..services.user_service import get_by_id

_not_found_message = f'Could not find user with the given id.'


def get_response(done: bool, error_message: str):
    if not done:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error_message)
    return None


async def raise_not_found_exception(result, message: str):
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)


async def result_verification(id: objectid) -> dict:
    result = await get_by_id(id)
    await raise_not_found_exception(result, message=_not_found_message)
    return result
