# project/tests/test_utils.py

import pytest
from bson import ObjectId
from fastapi import HTTPException, status
from app.helpers.utils import result_verification

# Mocking the get_by_id function for testing purposes
class MockUserService:
    @staticmethod
    async def get_by_id(id):
        # Simulating a database call where id='valid_id' returns a result and others return None
        if id == 'valid_id':
            return {'id': id, 'name': 'John Doe'}
        else:
            return None


@pytest.fixture
def mock_user_service(monkeypatch):
    # Replace the original get_by_id function with the mocked one
    monkeypatch.setattr('app.helpers.utils.get_by_id', MockUserService.get_by_id)


@pytest.mark.asyncio
async def test_result_verification_found(mock_user_service):
    # Test case where user with valid id is found
    id = 'valid_id'  # Replace with an actual ObjectId if needed
    result = await result_verification(id)
    assert result['name'] == 'John Doe'


@pytest.mark.asyncio
async def test_result_verification_not_found(mock_user_service):
    # Test case where user with invalid id is not found
    id = 'invalid_id'  # Replace with an actual ObjectId if needed
    with pytest.raises(HTTPException) as exc_info:
        await result_verification(id)

    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
    assert exc_info.value.detail == 'Could not find user with the given id.'
