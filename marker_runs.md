# 1. Сценарии прогонов

### pytest -m smoke
```
27 passed, 31 deselected, 1 xfailed in 0.10s 
```

### pytest -m regression
```
20 passed, 39 deselected in 0.09s
```

### pytest -m "smoke or regression"
```
47 passed, 11 deselected, 1 xfailed in 0.15s
```

### pytest -m "smoke and auth"
```
6 passed, 53 deselected in 0.04s
```

### pytest -m "not slow"
```
58 passed, 1 xfailed in 0.17s
```

### pytest -m storage
```
7 passed, 52 deselected in 0.05s
```

# 2. Сравнение smoke vs regression

### pytest -m smoke --durations=5 -vv
```
27 passed, 36 deselected, 1 xfailed in 0.08s
====================================== slowest 5 durations ========================================
0.00s setup    test_register_parametrized.py::test_register_with_valid_data_creates_user[standard]
0.00s setup    test_register_parametrized.py::test_register_with_valid_data_creates_user[with_dots]
0.00s setup    test_user_service_delete.py::test_delete_existing_user_removes_from_storage
0.00s setup    test_user_service_lifecycle.py::test_login_with_correct_credentials_returns_user
0.00s setup    test_user_service_lifecycle.py::test_get_user_returns_registered_user
```

### pytest -m smoke --durations=5 -vv
```
20 passed, 44 deselected in 0.08s
====================================== slowest 5 durations ========================================
0.00s setup    test_login_parametrized.py::test_login_with_invalid_credentials_raises[wrong_password]
0.00s setup    test_login_parametrized.py::test_login_with_invalid_credentials_raises[unknown_email]
0.00s call     test_user_service_delete.py::test_delete_one_user_keeps_others
0.00s setup    test_user_service_delete.py::test_delete_nonexistent_user_raises
0.00s setup    test_login_parametrized.py::test_login_with_invalid_credentials_raises[missing_digit]
```