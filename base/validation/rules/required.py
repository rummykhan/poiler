from base.validation.contracts.IRule import IRule


class Required(IRule):
    def validate(self, data):

        if data is None:
            return False

        if not data:
            return False

        data = data.strip()

        if len(data) is 0:
            return

        return True

    def get_message(self, field):
        return '{} is required'.format(field)
