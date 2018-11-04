__author__ = "woody"

class UserSchema(object):
    # 用户登录json_schema校验
    login_schema = {
        "type": "object",
        "properties": {
            "username": {
                "type": "string"
            },
            "password": {
                "type": "string"
            },
            "type": {
                "type": "string"
            }
        },
        "required": ["username", "password"]
    }

