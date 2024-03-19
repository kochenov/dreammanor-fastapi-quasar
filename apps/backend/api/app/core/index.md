## Настройка приложения

Этот код Python содержит класс `Settings`, который используется для определения конфигурации приложения.

Использование
-------------

-   Создайте файл `settings.py` и импортируйте класс `Settings` из этого модуля.
-   Создайте экземпляр класса `Settings`.
-   Доступ к значениям конфигурации можно получить через атрибуты экземпляра.

Пример
------

Python

```
from settings import Settings

settings = Settings()

# Доступ к значению API_V1_STR
api_v1_str = settings.API_V1_STR

# Доступ к значению BACKEND_CORS_ORIGINS
backend_cors_origins = settings.BACKEND_CORS_ORIGINS

```

Описание параметров
-------------------

API_V1_STR: Версия API (строка)

SECRET_KEY: Секретный ключ (генерируется автоматически)

ACCESS_TOKEN_EXPIRE_MINUTES: Время жизни токена доступа (в минутах)

DOMAIN: Домен приложения

ENVIRONMENT: Окружение (local, staging, production)

server_host: Хост сервера (вычисляется автоматически)

BACKEND_CORS_ORIGINS: Разрешенные CORS-домены (список или строка)

PROJECT_NAME: Название проекта

SENTRY_DSN: DSN для Sentry (необязательный)

POSTGRES_SERVER: Хост базы данных PostgreSQL

POSTGRES_PORT: Порт базы данных PostgreSQL

POSTGRES_USER: Пользователь базы данных PostgreSQL

POSTGRES_PASSWORD: Пароль пользователя базы данных PostgreSQL

POSTGRES_DB: База данных PostgreSQL

SQLALCHEMY_DATABASE_URI: Строка подключения к базе данных PostgreSQL (вычисляется автоматически)

SMTP_TLS: Использовать TLS для SMTP

SMTP_SSL: Использовать SSL для SMTP

SMTP_PORT: Порт SMTP-сервера

SMTP_HOST: Хост SMTP-сервера (необязательный)

SMTP_USER: Пользователь SMTP-сервера (необязательный)

SMTP_PASSWORD: Пароль пользователя SMTP-сервера (необязательный)

EMAILS_FROM_EMAIL: Адрес отправителя email (необязательный)

EMAILS_FROM_NAME: Имя отправителя email (необязательный)

_set_default_emails_from: Функция-валидатор, устанавливающая имя отправителя по умолчанию, если оно не задано.

EMAIL_RESET_TOKEN_EXPIRE_HOURS: Время жизни токена сброса пароля (в часах)

emails_enabled: Флаг, указывающий, включена ли отправка email (вычисляется автоматически)

EMAIL_TEST_USER: Тестовый адрес email (необязательный)

FIRST_SUPERUSER: Логин первого суперпользователя

FIRST_SUPERUSER_PASSWORD: Пароль первого суперпользователя

USERS_OPEN_REGISTRATION: Разрешена ли свободная регистрация пользователей

_check_default_secret: Функция, проверяющая, используется ли значение по умолчанию для секретных параметров.

_enforce_non_default_secrets: Функция-валидатор, проверяющая обязательную смену секретов по умолчанию после инициализации.