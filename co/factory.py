
from co import core, repositories

def create_user_service(user_repository=None):
    if user_repository is None:
        user_repository = repositories.InMemoryUserRepository()
    return core.UserService(user_repository)
