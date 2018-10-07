__auth__ = "woody"

from app import app


# 导入各个模块
from app.views.auth.User import user
app.register_blueprint(user)

if __name__ == '__main__':
    app.run()
