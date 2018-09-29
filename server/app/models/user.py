__author__ = "Woody"

'''
    sqlalchemy映射
'''

from . import db


class User(db.Model):
    id = db.Column(db.INT, primary_key=True)
    username = db.Column(db.String(99), unique=True)
    password = db.Column(db.String(99), unique=False)
    email = db.Column(db.String(99), unique=False)
    engineer = db.Column(db.String(99), unique=False)

    def __init__(self, username, password, email=None, engineer=None, id=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.engineer = engineer

    def __repr__(self):
        return '<User %r>' % self.username
