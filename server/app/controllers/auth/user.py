from .. import User


class UserUtil():

    @staticmethod
    def login():
        c = User.query.all()
        print(c)
