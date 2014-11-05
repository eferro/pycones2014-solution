
from co import core, repositories

def in_memory_user_repository():
    return repositories.InMemoryUserRepository()

def file_user_repository():
    return repositories.FileUserRepository('users.pickle')

def create_user_service(user_repository=None):
    if user_repository is None:
        user_repository = file_user_repository()
    return core.UserService(user_repository)
