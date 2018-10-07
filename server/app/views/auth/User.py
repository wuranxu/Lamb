from flask import Blueprint
from flask import jsonify
from flask import request
from ...controllers.auth.user import UserUtil

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/register")
def register():
    return jsonify({
"id": 26,
"type": "programming",
"setup": "If you put a million monkeys at a million keyboards, one of them will eventually write a Java program",
"punchline": "the rest of them will write Perl"
})

@user.route("/login")
def login():
    username =  request.args.get("username")
    password =  request.args.get("password")
    if username is not None and password is not None:
        UserUtil.login()
    return jsonify(dict(status=True))