
from co import errors


class User(object):
    def __init__(self, nickname):
        self.nickname = nickname
        self._followers = set()

    def add_follower(self, follower):
        self._followers.add(follower)

    def followers(self):
        return self._followers


class UserService(object):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register(self, nickname):
        if self.is_registered(nickname):
            raise errors.UserAlreadyRegisteredError()
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
