import pickle

class InMemoryUserRepository(object):
    def __init__(self):
        self._users = {}

    def find_by_nickname(self, nickname):
        return self._users.get(nickname)

    def put(self, user):
        self._users[user.nickname] = user


class FileUserRepository(object):
    def __init__(self, file_path):
        self.path = file_path
        try:
            self._users = pickle.load(open(self.path, "rb"))
        except IOError:
            self._users = {}

    def find_by_nickname(self, nickname):
        return self._users.get(nickname)


    def put(self, user):
        self._users[user.nickname] = user
        pickle.dump(self._users, open(self.path, "wb" ))
