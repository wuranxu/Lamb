# 基础配置类
import os

class Config(object):

    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'lamb.log')