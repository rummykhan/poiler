from base.log.logger import Logger
from base.support import command
from base.validation.validator import Validator


class BaseController(object):
    logger = None
    command = None
    verbosity = False

    def __init__(self, *args, **kwargs):
        self.logger = Logger()
        self.command = command

        if 'verbose' in kwargs:
            self.verbosity = kwargs['verbose']

    def validate(self, data: dict, rules: dict):
        return Validator(data, rules)

    def print(self, line):
        self.command.uprint(line)

    def info(self, line):

        if type(line) is not str:
            raise Exception("Invalid string.")

        self.logger.info(line)

    def warning(self, line):

        if type(line) is not str:
            raise Exception("Invalid string.")

        self.logger.warning(line)

    def error(self, line):

        if type(line) is not str:
            raise Exception("Invalid string.")

        self.logger.error(line)

    def success(self, line):

        if type(line) is not str:
            raise Exception("Invalid string.")

        self.logger.success(line)

    def verbose(self, line):

        if type(line) is not str:
            raise Exception("Invalid string.")

        if self.verbosity:
            self.info(line)
