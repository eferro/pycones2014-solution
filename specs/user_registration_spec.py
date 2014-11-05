
from expects import expect, be_true, raise_error

class UserService(object):
    def __init__(self):
        self._users = set()

    def register(self, nickname):
        self._users.add(nickname)

    def is_registered(self, nickname):
        return nickname in self._users


def create_user_service():
    return UserService()

with description('Register user'):

    with before.each:
        self.nickname = '@foolano'

    with it('registers a new user'):
        user_service = create_user_service()

        user_service.register(self.nickname)

        expect(user_service.is_registered(self.nickname)).to(be_true)

    with _context('when user already exists'):
        with it('raises error'):
            # Register a user
            pass
