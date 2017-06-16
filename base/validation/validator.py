from base.support.str import Str
from base.validation.contracts.IValidator import IValidator


class Validator(IValidator):
    data = None
    rules = None
    error_bag = []
    validated = False

    def __init__(self, data, rules):
        self.init(data, rules)

    def init(self, data, rules):
        self.data = data
        self.rules = rules

        if self.data is None:
            raise ValueError('Data cannot be null.')

        if self.rules is None:
            raise ValueError('Rules cannot be null.')

    def validate(self):

        for key, value in self.data.items():

            # mean user don't want to validate this field.
            if key not in self.rules:
                continue

            # validate each parameter.
            self.validateEach(key, value, self.rules[key])

        # Flag to check if validate has been called before
        self.validated = True

    def validateEach(self, key, value, rule):

        rules = rule.split('|')

        messages = []
        for rule in rules:
            try:
                instance = self.get_instance(rule)
            except:
                # In case we dont have that validator.. just raise the error..
                raise Exception("{} Validator not present.".format(rule))

            if instance.validate(value):
                return True

            messages.append(instance.get_message(key))

        self.error_bag.append({key: messages})

    def get_instance(self, rule):
        return globals()[Str.ucfirst(rule)]()

    def passes(self):
        if not self.validated:
            self.validate()

        return len(self.error_bag) == 0

    def get_message_bag(self):
        return self.error_bag
