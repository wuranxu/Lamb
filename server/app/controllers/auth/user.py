from .. import User
from .. import Team
from ...middleware.jwt import UserToken


class UserUtil(object):

    @staticmethod
    def login(user, pwd):
        user_info, token = None, None
        man = User.query.filter_by(username=user, password=pwd).first()
        if man is not None:
            # 生成token
            user_info = UserUtil.get_dict(man)
            team_info = Team.query.filter_by(id=man.team_id).first()
            if team_info is None:
                # 没有team归属 列为默认权限
                user_info["permission"] = "user"
            return user_info, UserToken.get_token(user_info)
        return user_info, token

    @staticmethod
    def get_dict(user_obj):
        return {c.name: getattr(user_obj, c.name) for c in user_obj.__table__.columns if c.name != 'password'}
