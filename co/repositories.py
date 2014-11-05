class InMemoryUserRepository(object):
    def __init__(self):
        self._users = {}

    def find_by_nickname(self, nickname):
        return self._users.get(nickname)

    def put(self, user):
        self._users[user.nickname] = user


class FileUserRepository(object):
    def find_by_nickname(self, nickname):
        pass

    def put(self, user):
        pass
