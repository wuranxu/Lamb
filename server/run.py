__auth__ = "woody"

from flask_cors import CORS

from app import app
# 导入各个模块
from app.views.auth.User import user

app.register_blueprint(user)

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(threaded=True)
