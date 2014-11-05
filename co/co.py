
def create_user_service():
    return UserService()

class UserAlreadyRegisteredError(Exception):
    pass

class UserService(object):
    def __init__(self):
        self._users = set()

    def register(self, nickname):
        if self.is_registered(nickname):
            raise UserAlreadyRegisteredError()
        self._users.add(nickname)

    def is_registered(self, nickname):
        return nickname in self._users

    def followers_for(self, nickname):
    	return []
