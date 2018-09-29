__author__ = 'Woody'

import mysql.connector as sql

from .. import app
from ..utils.logger import Log


class MysqlDb(object):
    """
        example:
        with MysqlDb() as db:
            rt = db.query(sql, params=())
    """

    def __init__(self):
        self.conn = sql.connect(host=app.config["MYSQL_HOST"], port=app.config["MYSQL_PORT"],
                                user=app.config["MYSQL_USER"], passwd=app.config["MYSQL_PWD"])
        self.cursor = self.conn.cursor(dictionary=True)    # 取出字典模式
        self.log = Log("mysqldb")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
        if exc_tb:
            self.log.error(str(exc_val))

    def close(self):
        self.cursor.close()
        self.conn.close()

    def query(self, sql, params=()):
        rv = None
        cursor = self.cursor
        try:
            cursor.execute(sql, params)
            rv = cursor.fetchall()
        except Exception as err:
            self.log.error('query: {}'.format(str(err)))
        return rv

    def operator(self, sql, params=()):
        rv = False
        cursor = self.cursor()
        try:
            cursor.execute(sql, params)
            self.conn.commit()
            rv = True
        except Exception as err:
            self.log.error('operate: {}'.format(str(err)))
        return rv