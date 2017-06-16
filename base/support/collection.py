import re

r"""Provides Support for Querying the Python Dictionary Lists.

This class helps in querying the list of dictionaries hence the name Collection.

e.g.

name_list = [{name: 'rehan', age: 27}, {name: 'manzoor', age: 28}, {name: 'yasir', age: 29}]

name_collection = Collection(name_list)

below_28 = name_collection.where('age', '<', 28).get()

Since where returns a collection object, We can chain methods too

c.where('x' '>', 5).where('name', 'rehan')

If two arguments are provided It will think of the middle argument as `=` operator

Supported Operators

    Equality Operators
        >       For greater than Comparison
        <       Fro less than Comparison
        >=      For greater than equal to.
        <=      For less than equal to.
        LIKE    For regex.
    
    Aggregation Operators
        sum     Get the sum of the specific field.
    
    Helpers
        first   Get the first item from the collection.
        last    Get the last item from the collection.
        count   Count the number of items in the collection.
"""


class Collection(object):
    # Collection list
    collection = None

    def __init__(self, collection):
        '''
        Collection is list of dictionary items.
        :param collection:
        '''
        self.collection = collection

    def where(self, *args):
        '''
        Args contain field, operator and value in the same order
        :param args:
        :return: self
        '''
        field, operator, value = self.get_query(args)
        return Collection(
            list(
                item for item in self.get_collection() if self.apply_where(item, field, operator, value)
            )
        )

    def apply_where(self, item, field, operator=None, value=None):
        '''
        It apply where on a single item.
        :param item:
        :param field:
        :param operator:
        :param value:
        :return:
        '''
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
        '''
        Checks if the field exists in the item.
        :param item:
        :param field:
        :return:
        '''
        return field in item

    def is_euqal(self, item, field, value):
        '''
        Checks if field of the item is equal to the value.
        :param item:
        :param field:
        :param value:
        :return:
        '''
        return self.if_exists(item, field) and item[field] == value

    def is_greater(self, item, field, value):
        '''
        Checks if field is > than the value.
        :param item:
        :param field:
        :param value:
        :return:
        '''
        return self.if_exists(item, field) and item[field] > value

    def is_smaller(self, item, field, value):
        '''
        Checks if field is < than the value.
        :param item:
        :param field:
        :param value:
        :return:
        '''
        return self.if_exists(item, field) and item[field] < value

    def is_smaller_equal(self, item, field, value):
        '''
        Checks if field is <= to the value.
        :param item:
        :param field:
        :param value:
        :return:
        '''
        return self.if_exists(item, field) and item[field] <= value

    def is_greater_equal(self, item, field, value):
        '''s
        Checks if field is >= to the value.
        :param item:
        :param field:
        :param value:
        :return:
        '''
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
        '''
        Get the last item of the collection.
        :return:
        '''
        try:
            return self.get_collection()[len(self.collection) - 1]
        except:
            return None

    def sum(self, field):
        '''
        Apply Sum on a field
        :param field:
        :return:
        '''
        return sum(item[field] for item in self.get_collection() if field in item)

    def get_collection(self):
        '''
        Get the collection as dictionary.
        :return:
        '''
        return self.collection

    def get_query(self, args):
        '''
        Parse the arguments to the query.
        :param args:
        :return:
        '''
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
        '''
        Count number of items in dictionary
        :return:
        '''
        return len(self.get_collection())

    def take(self, no_of_items=1):
        '''
        Take a sample from the collection.
        :param no_of_items:
        :return:
        '''
        if len(self.get_collection()) >= no_of_items:
            return Collection(self.get_collection()[no_of_items])

        return Collection(self.get_collection())
