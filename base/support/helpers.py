import json
import os
import re
import string
import sys
from urllib.parse import urlparse
from base.support import command

r""" Provides Helper Method

This module provide useful helper methods for the user.

Provided Methods:
    validate_url        Validate if the given string is a valid url.
    get_url             Get the url from the user.
    str_capitalize      Capitalize the string.
    try_json            Try to convert the string to JSON.
    change_title        Change title of the console window.
"""


def validate_url(val):
    '''
    Checks if the value is a valid url.
    :param val:
    :return:
    '''
    if val is None:
        return False

    if not val:
        return False

    tmp = urlparse(val)
    if tmp.scheme is '' or tmp.netloc is '':
        return False

    return True


def get_url():
    '''
    Get url from the User.
    :return:
    '''
    val = command.get_string_input('Enter URL :: ')
    if not validate_url(val):
        return get_url()
    return val


def str_capitalize(data):
    '''
    Capitalize the string.
    :param data:
    :return:
    '''
    if data is None:
        return data

    return string.capwords(data)


def try_json(response):
    '''
    Try converting a string to JSON
    :param response:
    :return:
    '''
    try:
        return json.loads(response)
    except:
        return {}


def change_title(title):
    '''
    Change title of the console.
    :param title:
    :return:
    '''
    if 'linux' in sys.platform:
        command = '\x1b]2;' + title + '\x07'
        sys.stdout.write(command)
        return

    if 'win' in sys.platform:
        command = 'TITLE %s' % str(title)
        os.system(command)
        return
