import sys


def get_yes_no(question):
    print('# %s' % question)
    val = input('Enter your choice y(yes), n(no) :: ')
    val = val.lower()
    if val.startswith('y'):
        return 'y'

    return 'n'


def get_string_input(question):
    val = input(question)
    if val.strip() is not '':
        return val

    return get_string_input(question)


def get_int_input(range):
    val = input('# Enter your choice :: ')

    try:
        val = int(val)
    except:
        print('# Wrong input.')
        return get_int_input(range)

    return val


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
