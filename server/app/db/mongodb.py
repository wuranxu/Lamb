__author__ = 'Woody'

import pymongo

from .. import app
from ..utils.logger import Log


class MongoClient(object):
    Client = None

    def __init__(self, db):
        try:
            self.Client = pymongo.MongoClient(host=app.config["MONGO_HOST"], port=app.config["MONGO_PORT"],
                                              maxPoolSize=app.config["MONGO_POOL"])
            self.db = self.Client[db]
            self.log = Log("mongodb")
            assert self.db.authenticate(app.config["MONGO_USER"], app.config["MONGO_PWD"]), "mongo服务器连接失败!"
        except Exception as err:
            raise Exception("mongo connect error: {}".format(str(err)))

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.Client is not None:
            self.Client.close()
        if exc_tb:
            self.log.error(str(exc_val))

    def __del__(self):
        self.Client.close()

    def close(self):
        self.Client.close()
