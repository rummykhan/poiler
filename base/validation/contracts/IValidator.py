class IValidator(object):

    def validate(self):
        raise NotImplementedError('Method not implemented')

    def passes(self):
        raise NotImplementedError('Method not implemented')

    def get_message_bag(self):
        raise NotImplementedError('Method not implemented')
