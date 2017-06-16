class IRule(object):
    def validate(self, data):
        raise NotImplementedError("Method not implemented.")

    def get_message(self, field):
        raise NotImplementedError("Method not implemented.")
