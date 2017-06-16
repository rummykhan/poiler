from base.log.contract.logger import ILogger
from base.support import command


class Logger(ILogger):
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    SUCCESS = 'SUCCESS'

    command = None

    def __init__(self):
        self.command = command

    def info(self, log, data=None):
        self.log(log, Logger.INFO, data)

    def warning(self, log, data=None):
        self.log(log, Logger.WARNING, data)

    def error(self, log, data=None):
        self.log(log, Logger.ERROR, data)

    def success(self, log, data=None):
        self.log(log, Logger.SUCCESS, data)

    def log(self, log, level, data=None):
        if level == Logger.INFO:
            self.command.uprint("[{}] {}".format(Logger.INFO, log))
        elif level == Logger.WARNING:
            self.command.uprint("[{}] {}".format(Logger.WARNING, log))
        elif level == Logger.ERROR:
            self.command.uprint("[{}] {}".format(Logger.ERROR, log))
        elif level == Logger.SUCCESS:
            self.command.uprint("[{}] {}".format(Logger.SUCCESS, log))
        else:
            raise Exception('Log Level is not defined')
