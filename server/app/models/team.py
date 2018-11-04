__author__ = "Woody"

'''
    团队表映射
'''

from . import db


class Team(db.Model):
    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String(99), unique=True, nullable=False)
    owner_id = db.Column(db.INT, unique=False, nullable=False)  # 所有人
    permission_id = db.Column(db.INT, unique=False)  # 关联权限表
    create_time = db.Column(db.DateTime, unique=False)  # 创建时间

    def __init__(self, name, owner_id, permission_id=None):
        self.name = name
        self.owner_id = owner_id
        self.permission_id = permission_id

    def __repr__(self):
        return '<Team %r>' % self.name
