'''
    这是一个装饰器方法文件
'''

from functools import wraps

from flask import jsonify, request
from jsonschema import validate, FormatChecker, ValidationError

from ..middleware.jwt import UserToken


class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance == None:
            self.instance = self.cls(*args, **kwds)
        return self.instance


def schema(sc):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if request.get_json() is not None:
                    validate(request.get_json(), sc, format_checker=FormatChecker())
                else:
                    raise Exception("请求json参数不合法")
            except ValidationError as e:
                return jsonify(dict(code=102, msg=str(e.message)))  # 返回参数校验失败信息
            except Exception as e:
                return jsonify(dict(code=101, msg=str(e)))
            return func(*args, **kwargs)

        return wrapper

    return decorator


def token_expired(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            headers = request.headers
            token = headers.get('token')
            if token is None:
                return jsonify(dict(code=403, msg="用户token认证失败, 请检查"))
            kwargs["user_info"] = UserToken.parse_token(token)
        except Exception as e:
            return jsonify(dict(code=403, msg=str(e)))
        return func(*args, **kwargs)

    return wrapper
