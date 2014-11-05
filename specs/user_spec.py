from co import co
from expects import expect, be_empty, contain_exactly, be_false, raise_error


with description('User'):

    with before.each:
        self.nickname = '@foolano'
        self.follower = '@futano'
        self.follower2 = '@futano2'
        self.user_service = co.create_user_service()

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
