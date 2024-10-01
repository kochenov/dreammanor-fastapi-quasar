from fastapi_users.authentication import BearerTransport

# TODO: вынести в настройки
bearer_transport = BearerTransport(tokenUrl="/api/v1/auth-service/login")
