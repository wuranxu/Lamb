from datetime import timedelta, datetime

import jwt
from jwt.exceptions import ExpiredSignatureError


class UserToken(object):
    key = 'LambToken'
    expired_time = 3

    @staticmethod
    def get_token(data):
        new_data = dict({"exp": datetime.utcnow() + timedelta(hours=UserToken.expired_time)}, **data)
        return jwt.encode(new_data, key=UserToken.key).decode()

    @staticmethod
    def parse_token(token):
        try:
            return jwt.decode(token, key=UserToken.key)
        except ExpiredSignatureError:
            raise Exception("token已过期, 请重新登录")
