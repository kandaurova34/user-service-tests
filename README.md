# User Service — автотесты на pytest

Учебный проект курса AQA. Автотесты на сервис работы с пользователями:
регистрация, логин, удаление, валидация email и пароля.

## Стек

- Python 3.x
- pytest
- pytest-cov

## Структура проекта
```
user-service-tests/
├── .gitignore                 ← что не коммитить
├── README.md                  ← описание проекта, инструкция
├── pytest.ini                 ← конфигурация pytest
├── requirements.txt           ← зависимости
├── src/
│   ├── user_service.py        ← User, UserService, исключения
│   └── validators.py          ← валидация email и пароля
└── tests/
    ├── conftest.py            ← sys.path для src/ + valid_credentials 
    ├── unit/
    │   ├── test_validators.py
    │   └── test_user_model.py
    └── integration/
        └── conftest.py         ← storage_file, user_service, registered_user
        └── test_environment_features.py
        └── test_login_parametrized.py
        └── test_register_parametrized.py
        └── test_scope_experiment.py
        └── test_user_service_basic.py
        └── test_user_service_delete.py
        └── test_user_service_lifecycle.py
        └── test_validators_env.py
```

## Установка и запуск
### Установка
1. Клонировать репозиторий
```
git clone https://github.com/kandaurova34/user-service-tests.git
cd user-service-tests
```
2. Создать и активировать виртуальное окружение
```
python3 -m venv venv
source venv/bin/activate          # macOS / Linux
```
или
```
venv\Scripts\Activate.ps1         # Windows PowerShell
```
3. Установить зависимости
```
pip install -r requirements.txt
```
4. Запустить все тесты
```
pytest
```

### Запуск
1. Только unit-тесты
```
pytest tests/unit/
```
2. Только integration-тесты
```
pytest tests/integration/
```
3. Только smoke-тесты
```
pytest -m smoke
```
4. Только regression в integration
```
pytest tests/integration/ -m regression
```
5. С покрытием кода
```
pytest --cov=src
```
6. С подробным отчётом по покрытию (какие строки не покрыты)
```
pytest --cov=src --cov-report=term-missing
```

## Маркеры

- smoke — критичные тесты, прогон после каждого деплоя
- regression — полный регрессионный набор
- validators / auth / storage — функциональные категории
- slow — медленные тесты

## Что покрыто тестами

- Валидация email и пароля (классы эквивалентности, граничные значения)
- Регистрация: happy path, дубликаты, невалидные данные
- Логин: правильные/неправильные креды, несуществующий email
- Удаление: существующий/несуществующий пользователь
- Покрытие кода: 97% (см. pytest --cov=src)