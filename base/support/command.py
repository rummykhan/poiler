import sys

r""" Provides Support for User Interaction.

This module helps in manipulating User Interaction.
e.g.

1. Asking Question from user.
2. Taking input from user.
3. Asking if User confirms.
4. Printing a string which contains Non-ASCII Characters.

This module is also inspired from Symfony/Command Object.


"""


def confirm(question=None):
    '''
    Display a Question to User and check if he comply or not.
    :param question:
    :return:
    '''
    val = input(" > {} Are you sure? y(yes), n(no) :: ".format(question))
    val = val.lower()

    if val.startswith('y'):
        return True

    return confirm(question)


def get_string_input(question):
    '''
    Get string input from the user.
    :param question:
    :return:
    '''
    val = input(" > {}".format(question))
    if val.strip() is not '':
        return val

    return get_string_input(question)


def get_int_input(range):
    '''
    Get Integer input from the user which is in given range.
    :param range:
    :return:
    '''
    val = input(' > Enter your choice :: ')

    try:
        val = int(val)
    except:
        print('# Wrong input.')
        return get_int_input(range)

    return val


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    '''
    Print a stream which consists of Non-ASCII or Non-Printable Characters.
    :param objects:
    :param sep:
    :param end:
    :param file:
    :return:
    '''
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
