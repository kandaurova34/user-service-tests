import pytest
from user_service import UserNotFoundError

@pytest.mark.smoke
@pytest.mark.storage
def test_delete_existing_user_removes_from_storage (user_service, registered_user):
    user_service.delete_user("alice@example.com")
    assert user_service.count_users() == 0

@pytest.mark.regression
@pytest.mark.storage
def test_delete_existing_user_makes_get_return_none(user_service, registered_user):
    user_service.delete_user("alice@example.com")
    assert user_service.get_user("alice@example.com") is None

@pytest.mark.regression
@pytest.mark.storage
def test_delete_nonexistent_user_raises (user_service, registered_user):
    with pytest.raises(UserNotFoundError):
        user_service.delete_user("ghost@example.com")

@pytest.mark.regression
@pytest.mark.storage
def test_delete_one_user_keeps_others (user_service, registered_user):
    user_service.register("mark@example.com", "Password123!")
    user_service.register("inna@example.com", "Password123!")
    user_service.delete_user("mark@example.com")
    assert user_service.count_users() == 2