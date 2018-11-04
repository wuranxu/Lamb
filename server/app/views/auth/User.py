from flask import Blueprint
from flask import jsonify
from flask import request

from ..auth.UserSchema import UserSchema
from ...controllers.auth.user import UserUtil
from ...utils.decorator import schema, token_expired

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/login", methods=("POST",))
@schema(UserSchema.login_schema)
def login():
    data = request.get_json()
    user_info, token = UserUtil.login(data.get("username"), data.get("password"))
    if user_info is None:
        return jsonify(dict(code=500, msg="用户名或密码错误"))
    return jsonify(dict(code=200, msg="登录成功", token=token, **user_info))


@user.route("/info")
@token_expired
def get_user_info(user_info):
    return jsonify(user_info)  # 获取User表信息
