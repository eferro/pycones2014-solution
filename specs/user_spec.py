from co import core, factory, errors
from expects import expect, be_empty, be_true, contain_exactly, be_false, raise_error


with description('Register user'):

    with before.each:
        self.nickname = '@foolano'
        self.user_service = factory.create_user_service(factory.in_memory_user_repository())

    with it('initialy a user is not registered'):
        expect(self.user_service.is_registered('irrelevant_ninckname')).to(be_false)

    with it('registers a new user'):
        self.user_service.register(self.nickname)

        expect(self.user_service.is_registered(self.nickname)).to(be_true)

    with context('when user already exists'):
        with it('raises error'):
            self.user_service.register(self.nickname)

            expect(lambda: self.user_service.register(self.nickname)).to(raise_error(errors.UserAlreadyRegisteredError))


with description('User followers'):

    with before.each:
        self.nickname = '@foolano'
        self.follower = '@futano'
        self.follower2 = '@futano2'
        self.user_service = factory.create_user_service(factory.in_memory_user_repository())

    with it('initialy a user have no followers'):
        expect(self.user_service.followers_for(self.nickname)).to(be_empty)

    with it('register a follower'):
        self.user_service.register(self.nickname)
        self.user_service.add_follower(self.nickname, follower=self.follower)

        expect(self.user_service.followers_for(self.nickname)).to(contain_exactly(self.follower))

    with it('register two followers'):
        self.user_service.register(self.nickname)
        self.user_service.add_follower(self.nickname, follower=self.follower)
        self.user_service.add_follower(self.nickname, follower=self.follower2)

        expect(self.user_service.followers_for(self.nickname)).to(contain_exactly(self.follower, self.follower2))


with description('User cos'):

    with before.each:
        self.nickname = '@foolano'
        self.user_service = factory.create_user_service(factory.in_memory_user_repository())

    with it('initialy a user have no cos'):
        self.user_service.register(self.nickname)

        expect(self.user_service.cos_for(self.nickname)).to(be_empty)

    with it('register a co for a nickname'):
        self.user_service.register(self.nickname)

        self.user_service.add_co(self.nickname, 'a_co1')
        self.user_service.add_co(self.nickname, 'a_co2')

        expect(self.user_service.cos_for(self.nickname)).to(contain_exactly('a_co1', 'a_co2'))
