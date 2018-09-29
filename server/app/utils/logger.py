import logbook

from .decorator import SingletonDecorator
from .. import app


@SingletonDecorator
class Log(object):
    handler = None

    def __init__(self, name='app', filename=app.config['LOG_NAME']):  # Logger标识默认为app
        self.handler = logbook.FileHandler(filename, encoding='utf-8')
        logbook.set_datetime_format("local")  # 将日志时间设置为本地时间
        self.logger = logbook.Logger(name)
        self.handler.push_application()

    def info(self, *args, **kwargs):
        return self.logger.info(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.logger.error(*args, **kwargs)

    def warning(self, *args, **kwargs):
        return self.logger.warning(*args, **kwargs)

    def debug(self, *args, **kwargs):
        return self.logger.debug(*args, **kwargs)
