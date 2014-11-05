
from co import co
from expects import expect, be_true, be_false, raise_error






with description('Register user'):

    with before.each:
        self.nickname = '@foolano'
        self.user_service = co.create_user_service()

    with it('initialy a user is not registered'):
        expect(self.user_service.is_registered('irrelevant_ninckname')).to(be_false)

    with it('registers a new user'):
        self.user_service.register(self.nickname)

        expect(self.user_service.is_registered(self.nickname)).to(be_true)

    with context('when user already exists'):
        with it('raises error'):
            self.user_service.register(self.nickname)

            expect(lambda: self.user_service.register(self.nickname)).to(raise_error(co.UserAlreadyRegisteredError))
