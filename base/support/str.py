import re


class Str(object):
    @staticmethod
    def to_ascii(data):
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

        string = Str.to_ascii(string)

        if len(string) <= length:
            return string

        return string[:length] + end_char

    @staticmethod
    def ucfirst(string):

        if string is None:
            return ''

        if len(string) < 2:
            return string

        return string[0].upper() + string[1:]

    @staticmethod
    def contains(haystack, needle):
        return needle in haystack

    @staticmethod
    def get_string_after(haystack, after, to=None):

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
