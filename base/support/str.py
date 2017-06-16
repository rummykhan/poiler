import re

r""" Provides Support For String Manipulation

This module provides support for string manipulation.

Supported Methods

    to_ascii            Extract Only ASCII from a mixed stream.
    limit               Get the limited number of characters.
    ucfirst             Capitalize Only first letter of the string.
    contains            Checks if a string contains another string.
    get_string_after    Get string after a word or a character.
"""

class Str(object):

    @staticmethod
    def to_ascii(data):
        '''
        Get the Pure ASCII characters from a mixed stream.
        :param data:
        :return:
        '''
        if data is None:
            return data
        p = re.compile('[\x00-\x7F]+')
        results = re.findall(p, data)

        output = ''
        if len(results) > 0:
            for result in results:
                output += result

            return output

        return ''

    @staticmethod
    def limit(string, length, end_char='...'):
        '''
        Get the limited number of characters from the string.
        :param string:
        :param length:
        :param end_char:
        :return:
        '''
        string = Str.to_ascii(string)

        if len(string) <= length:
            return string

        return string[:length] + end_char

    @staticmethod
    def ucfirst(string):
        '''
        Conver the first letter of the string to uppercase.
        :param string:
        :return:
        '''
        if string is None:
            return ''

        if len(string) < 2:
            return string

        return string[0].upper() + string[1:]

    @staticmethod
    def contains(haystack, needle):
        '''
        Checks if a string contains another string.
        :param haystack:
        :param needle:
        :return:
        '''
        return needle in haystack

    @staticmethod
    def get_string_after(haystack, after, to=None):
        '''
        Get a substring from another string based on string.
        :param haystack:
        :param after:
        :param to:
        :return:
        '''
        if haystack is None or after is None:
            raise Exception('Either haystack or after is None.')

        if not Str.contains(haystack, after):
            return None

        output = haystack[haystack.find(after) + len(after):]

        if to is None:
            return output

        if to < len(output):
            return output[0:to]

        return None
