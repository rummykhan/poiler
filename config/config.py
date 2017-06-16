import json
import os

from base.support.map import Map


class Config(object):
    @staticmethod
    def get(path, default=None, config_file='/config/config.json'):

        file_contents = Config.get_contents(config_file)

        if file_contents is None:
            return default

        return Config.get_value(file_contents, path, default)

    @staticmethod
    def get_value(dict_object, path, default):

        try:
            index, key = path.split('.', 1)
        except:
            index, key = path, ''

        map = Map(dict_object)

        if index not in map:
            return default

        if len(key) > 0:
            return Config.get_value(map[index], key, default)

        if index in map:
            return map[index]

        return default

    @staticmethod
    def get_contents(config_file=None):
        file_contents = None

        with open(os.path.join(os.getcwd()) + config_file) as reader:
            file_contents = json.loads(reader.read())

        if file_contents is None:
            return None

        return file_contents
