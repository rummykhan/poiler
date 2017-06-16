import json
import os

from base.support.map import Map

r""" Provides Support for reading JSON based configuration files.

This module helps in reading JSON based configuration files.


e.g.

config.json

{
    database:{
        username: 'root',
        pass: 'root'
    }
}

You can get the username like

Config.get('database.username')


This module expose 3 static methods, Out of which use of only two is recommended.

    get             get reads the json config contents recursively and gets the value using . notation path.
    get_value       get value takes two parameters dictionary object and path to the final key.

"""


class Config(object):
    @staticmethod
    def get(path, default=None, config_file='/config/config.json'):
        '''
        Read the contents of the Configuration file and return the value
        based on . notation path.
        :param path:
        :param default:
        :param config_file:
        :return:
        '''
        file_contents = Config.get_contents(config_file)

        if file_contents is None:
            return default

        return Config.get_value(file_contents, path, default)

    @staticmethod
    def get_value(dict_object, path, default):
        '''
        Get value from dictionary based on . notation path.
        :param dict_object:
        :param path:
        :param default:
        :return:
        '''
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
        '''
        Get contents of the file and convert these to json.
        :param config_file:
        :return:
        '''
        file_contents = None

        with open(os.path.join(os.getcwd()) + config_file) as reader:
            file_contents = json.loads(reader.read())

        if file_contents is None:
            return None

        return file_contents
