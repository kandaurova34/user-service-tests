import pytest
from user_service import UserService, UserNotFoundError

@pytest.fixture
def user_service(tmp_path):
    storage = tmp_path / "users.json"
    storage.write_text("{}")
    service = UserService(storage_path=storage)

    yield service

    # teardown — после теста
    # tmp_path сам почистится, но для тренировки явно сбросим файл
    if storage.exists():
        storage.write_text("{}")

@pytest.fixture
def registered_user(user_service):
    email = "alice@example.com"
    password = "Password123"
    user_service.register(email, password)
    return {"email": email, "password": password}

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