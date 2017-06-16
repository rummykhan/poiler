import json
import operator
import os
import re
import string
import sys
from urllib.parse import urlparse

from base.support import command


def validate_url(val):
    if val is None:
        return False

    if not val:
        return False

    tmp = urlparse(val)
    if tmp.scheme is '' or tmp.netloc is '':
        return False

    return True


def get_url():
    val = command.get_string_input('Enter URL :: ')
    if not validate_url(val):
        return get_url()
    return val


def sort_locations(locations):
    locations = sorted(locations.items(), key=operator.itemgetter(0))
    most = locations[len(locations) - 1]
    return most[1]['name']


def purify_string(data):
    if data is None:
        return data

    data = str(data)

    data = get_pure_ascii(data)

    if data is None:
        return data

    data = str_strip(data)

    return data.replace('\n', '')


def str_strip(data, to_strip=' '):
    return data.strip(to_strip)


def get_pure_ascii(data):
    if data is None:
        return data

    p = re.compile('[\x00-\x7F]+')

    results = re.findall(p, data)

    output = ''
    if len(results) > 0:
        for result in results:
            output += result

        return output

    return None


def get_pure_email(data):
    if data is None:
        return data

    data = str_strip(data)
    data = str_strip(data, ',')
    data = data.lower()

    return data


def get_pure_phone(data):
    if data is None:
        return data

    data = str(data)

    data = str_strip(data)
    data = data.replace(' ', '')
    data = data.replace('-', '')
    data = data.replace('(', '')
    data = data.replace(')', '')

    return check_plus_sign(data)


def check_plus_sign(data):
    index = -1
    try:
        index = data.index('+')
    except:
        index = -1

    if index is -1:
        return '+' + data


def get_pure_amount(data):
    if data is None:
        return data

    data = str(data)
    data = str_strip(data)
    data = data.replace(' ', '')
    data = data.replace(',', '')

    try:
        return int(data)
    except:
        return 0


def str_capitalize(data):
    if data is None:
        return data

    return string.capwords(data)


def get_json(html):
    if html is None:
        return None

    finder_text_start = '<script type="text/javascript">window._sharedData = '
    finder_text_start_len = len(finder_text_start) - 1
    finder_text_end = ';</script>'

    all_data_start = html.find(finder_text_start)
    all_data_end = html.find(finder_text_end, all_data_start + 1)
    json_str = html[(all_data_start + finder_text_start_len + 1): all_data_end]

    return try_json(json_str)


def try_json(response):
    try:
        return json.loads(response)
    except:
        return {}


def change_title(title):
    if 'linux' in sys.platform:
        command = '\x1b]2;' + title + '\x07'
        sys.stdout.write(command)
        return

    if 'win' in sys.platform:
        command = 'TITLE %s' % str(title)
        os.system(command)
        return


def get_summary(influencer):
    if 'summaries' not in influencer:
        return None

    for summary in influencer['summaries']:
        if 'channel' not in summary:
            continue

        if summary['channel'] == 'ednrd':
            return summary

    return None
