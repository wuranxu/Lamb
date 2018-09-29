# 基础配置类
import os

class Config(object):

    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'lamb.log')
    JSON_AS_ASCII = False   # Flask jsonify编码问题

    # MONGODB配置
    MONGO_HOST = "127.0.0.1"
    MONGO_PORT = 27017
    MONGO_USER = "admin"
    MONGO_PWD = "admin"
    MONGO_POOL = 200

    # MYSQL配置
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = "wuranxu"
    DBNAME = "test"

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
                                    MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = False     # 消除sqlalchemy警告