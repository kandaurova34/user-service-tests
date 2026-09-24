# Structure verification

### pytest
```
================================================================================================= short test summary info =================================================================================================
SKIPPED [1] tests/integration/test_environment_features.py:5: Функционал ещё не реализован: восстановление пароля
XFAIL tests/integration/test_environment_features.py::test_greet_user_returns_greeting - QA-5678: функция greet_user ещё не реализована
XFAIL tests/integration/test_environment_features.py::test_register_empty_email_raises_value_error_specifically - QA-9012: ожидаем ValueError при пустом email
XFAIL tests/unit/test_validators.py::test_is_valid_email[invalid_double_dot_in_domain_QA1234] - QA-1234: двойная точка в домене не должна проходить
======================================================================================== 60 passed, 1 skipped, 3 xfailed in 0.18s =========================================================================================
```

### pytest tests/unit/
```
================================================================================================= short test summary info =================================================================================================
XFAIL tests/unit/test_validators.py::test_is_valid_email[invalid_double_dot_in_domain_QA1234] - QA-1234: двойная точка в домене не должна проходить
============================================================================================== 23 passed, 1 xfailed in 0.06s ==============================================================================================
```

### pytest tests/integration/
```
================================================================================================= short test summary info =================================================================================================
SKIPPED [1] tests/integration/test_environment_features.py:5: Функционал ещё не реализован: восстановление пароля
XFAIL tests/integration/test_environment_features.py::test_greet_user_returns_greeting - QA-5678: функция greet_user ещё не реализована
XFAIL tests/integration/test_environment_features.py::test_register_empty_email_raises_value_error_specifically - QA-9012: ожидаем ValueError при пустом email
======================================================================================== 37 passed, 1 skipped, 2 xfailed in 0.14s =========================================================================================
```

### pytest -m smoke
```
================================================================================================= short test summary info =================================================================================================
XFAIL tests/unit/test_validators.py::test_is_valid_email[invalid_double_dot_in_domain_QA1234] - QA-1234: двойная точка в домене не должна проходить
====================================================================================== 27 passed, 36 deselected, 1 xfailed in 0.10s =======================================================================================
```

### pytest tests/integration/ -m regression
```
============================================================================================ 20 passed, 20 deselected in 0.08s ============================================================================================
```