import re


class Collection(object):
    # Collection list
    collection = None

    # Initialize the constructor
    def __init__(self, collection):
        self.collection = collection

    # where clause for the Collection
    def where(self, *args):
        field, operator, value = self.get_query(args)
        return Collection(
            list(
                item for item in self.get_collection() if self.apply_where(item, field, operator, value)
            )
        )

    # Apply Where Clause
    def apply_where(self, item, field, operator=None, value=None):
        if operator is '>':
            return self.is_greater(item, field, value)
        elif operator is '<':
            return self.is_smaller(item, field, value)
        elif operator is '>=':
            return self.is_greater_equal(item, field, value)
        elif operator is '<=':
            return self.is_smaller_equal(item, field, value)
        elif operator is 'LIKE':
            return self.is_like(item, field, value)

        return self.is_euqal(item, field, value)

    def if_exists(self, item, field):
        return field in item

    def is_euqal(self, item, field, value):
        return self.if_exists(item, field) and item[field] == value

    def is_greater(self, item, field, value):
        return self.if_exists(item, field) and item[field] > value

    def is_smaller(self, item, field, value):
        return self.if_exists(item, field) and item[field] < value

    def is_smaller_equal(self, item, field, value):
        return self.if_exists(item, field) and item[field] <= value

    def is_greater_equal(self, item, field, value):
        return self.if_exists(item, field) and item[field] >= value

    def is_like(self, item, field, value):
        return self.if_exists(item, field) and re.search(value, item[field])

    def get(self):
        return self.get_collection()

    def first(self):
        try:
            return self.collection[0]
        except:
            return None

    def last(self):
        try:
            return self.get_collection()[len(self.collection) - 1]
        except:
            return None

    def sum(self, field):
        return sum(item[field] for item in self.get_collection() if field in item)

    def get_collection(self):
        return self.collection

    def get_query(self, args):

        if len(args) < 2:
            raise Exception("Query arguments are not enough.")

        field = args[0]
        operator = '='
        value = args[1]

        if len(args) > 2:
            operator = args[1]
            value = args[2]

        return field, operator, value

    def count(self):
        return len(self.get_collection())

    def take(self, no_of_items=1):

        if len(self.get_collection()) >= no_of_items:
            return Collection(self.get_collection()[no_of_items])

        return Collection(self.get_collection())
