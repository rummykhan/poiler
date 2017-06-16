class Dict(object):
    @staticmethod
    def unpack(nodes):
        tmp_storage = []

        for node in nodes:
            tmp_storage.append(Dict.walk_recursive(node))

        return tmp_storage

    @staticmethod
    def set(map, key, value, parent):

        if parent is not None:
            key = "{}_{}".format(parent, key)

        map[key] = value

        return map

    @staticmethod
    def walk_recursive(dictionary, map=None, parent=None):

        if map is None:
            map = {}

        for key, value in dictionary.items():

            if isinstance(value, dict):

                if parent is not None:
                    map = Dict.walk_recursive(value, map, "{}_{}".format(parent, key))
                else:
                    map = Dict.walk_recursive(value, map, key)

                continue

            map = Dict.set(map, key, value, parent)

        return map
