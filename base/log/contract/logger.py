class ILogger(object):
    def info(self, log, data=None):
        raise NotImplementedError('Method not implemented')

    def error(self, log, data=None):
        raise NotImplementedError('Method not implemented')

    def warning(self, log, data=None):
        raise NotImplementedError('Method not implemented')

    def success(self, log, data=None):
        raise NotImplementedError('Method not implemented')

    def log(self, log, level, data=None):
        raise NotImplementedError('Method not implemented')
