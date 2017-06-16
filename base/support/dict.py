r"""Provides Support for Dictionary List Manipulation.

Recursively walk over a  Dictionary of python and combine the keys by a joiner.

e.g.

dict = {
    name: "rehan",
    schooling: {
        masters : "PAF KIET"
    }
}


d = Dict.walk_recursive(dict)

print(d)

{ name: 'rehan', 'schooling_masters': 'PAF KIET'}

"""


class Dict(object):
    @staticmethod
    def unpack(nodes):
        '''
        Iterate over a list of dictionaries.
        :param nodes:
        :return:
        '''
        tmp_storage = []

        for node in nodes:
            tmp_storage.append(Dict.walk_recursive(node))

        return tmp_storage

    @staticmethod
    def set(map, key, value, parent, joiner='_'):
        '''
        Add a Key to the dictionary.
        :param map:
        :param key:
        :param value:
        :param parent:
        :param joiner:
        :return:
        '''
        if parent is not None:
            key = "{}{}{}".format(parent, joiner, key)

        map[key] = value

        return map

    @staticmethod
    def walk_recursive(dictionary, map=None, parent=None, joiner='_'):
        '''
        Walk over a dictionary recursively.
        :param dictionary:
        :param map:
        :param parent:
        :param joiner:
        :return:
        '''
        if map is None:
            map = {}

        for key, value in dictionary.items():

            if isinstance(value, dict):

                if parent is not None:
                    map = Dict.walk_recursive(value, map, "{}{}{}".format(parent, joiner, key), joiner)
                else:
                    map = Dict.walk_recursive(value, map, key, joiner)

                continue

            map = Dict.set(map, key, value, parent, joiner)

        return map
