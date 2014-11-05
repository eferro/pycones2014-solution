import os
from co import factory
from expects import expect, be_true, contain_exactly


with description('Persistence'):

    with before.each:
        self.nickname = '@foolano'
        self.follower = '@futano'
        self.follower2 = '@futano2'
        try:
            os.remove('users.pickle')
        except OSError:
            pass

    with it('persist users'):
        user_service = factory.create_user_service()
        user_service.register(self.nickname)

        new_user_service = factory.create_user_service()
        expect(new_user_service.is_registered(self.nickname)).to(be_true)

    with it('persist followers'):
        user_service = factory.create_user_service()
        user_service.register(self.nickname)
        user_service.add_follower(self.nickname, follower=self.follower)
        user_service.add_follower(self.nickname, follower=self.follower2)

        new_user_service = factory.create_user_service()
        expect(new_user_service.followers_for(self.nickname)).to(contain_exactly(self.follower, self.follower2))
