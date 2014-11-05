
class InMemoryUserRepository(object):
    def __init__(self):
        self._users = {}

    def find_by_nickname(self, nickname):
        return self._users.get(nickname)

    def put(self, user):
        self._users[user.nickname] = user

class User(object):
    def __init__(self, nickname):
        self.nickname = nickname
        self._followers = set()

    def add_follower(self, follower):
        self._followers.add(follower)

    def followers(self):
        return self._followers


def create_user_service(user_repository=None):
    if user_repository is None:
        user_repository = InMemoryUserRepository()
    return UserService(user_repository)

class UserAlreadyRegisteredError(Exception):
    pass


class UserService(object):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register(self, nickname):
        if self.is_registered(nickname):
            raise UserAlreadyRegisteredError()
        self.user_repository.put(User(nickname))

    def is_registered(self, nickname):
        return self.user_repository.find_by_nickname(nickname) is not None

    def followers_for(self, nickname):
        user = self.user_repository.find_by_nickname(nickname)
        return user.followers() if user else []

    def add_follower(self, nickname, follower):
        user = self.user_repository.find_by_nickname(nickname)
        if user is not None:
            user.add_follower(follower)
            self.user_repository.put(user)
