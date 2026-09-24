import pytest
from user_service import InvalidCredentialsError

@pytest.mark.smoke
@pytest.mark.storage
def test_user_service_starts_empty (user_service):
    assert user_service.count_users() == 0

@pytest.mark.smoke
@pytest.mark.auth
def test_user_service_count_increases_after_register (user_service):
    user_service.register("alice@example.com", "Password123!")
    assert user_service.count_users() == 1

@pytest.mark.regression
@pytest.mark.auth
def test_user_service_count_increases_for_multiple_users (user_service):
    user_service.register("mark@example.com", "Password123!")
    user_service.register("inna@example.com", "Password123!")
    user_service.register("job@example.com", "Password123!")
    assert user_service.count_users() == 3

@pytest.mark.smoke
@pytest.mark.auth
def test_login_with_correct_credentials_returns_user (user_service, registered_user):
    user = user_service.login(registered_user["email"], registered_user["password"])
    assert user.email == registered_user["email"]

@pytest.mark.regression
@pytest.mark.auth
def test_login_with_wrong_password_raises (user_service, registered_user):
    with pytest.raises(InvalidCredentialsError):
        user_service.login(registered_user["email"], "WrongPass1")

@pytest.mark.regression
@pytest.mark.auth
def test_login_with_nonexistent_email_raises (user_service, registered_user):
    with pytest.raises(InvalidCredentialsError):
        user_service.login("ghost@example.com", registered_user["password"])

@pytest.mark.smoke
@pytest.mark.storage
def test_get_user_returns_registered_user (user_service, registered_user):
    user = user_service.login(registered_user["email"], registered_user["password"],)
    assert user.email == registered_user["email"]

@pytest.mark.regression
@pytest.mark.storage
def test_get_user_returns_none_for_unknown_email (user_service, registered_user):
    user = user_service.get_user("ghost@example.com")
    assert user is None