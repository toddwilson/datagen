from datagen import field_type, field_arg
from random import randint, choice, random
import sys
from time import strptime, mktime, strftime, localtime


if sys.version_info.major == 2:
    from string import lowercase
    from string import uppercase
    lc_set = lowercase + uppercase
elif sys.version_info.major == 3:
    from string import ascii_letters as lc_set

method_dispatch = {}


def arg_parser(arg):
    arglist = [a.split('=') for a in arg.replace(' ', '').split(',')]

    args = {}
    for pack in arglist:
        if len(pack) == 1:
            args[pack[0]] = None
        else:
            args[pack[0]] = pack[1]

    return args


@field_type(name="bool")
def bool_field(arg):
    return choice((1, 0))


@field_type(name="int")
def integer_field(length):
    return randint(0, length)


@field_arg(name="int")
def integer_field_argument(arg):
    return int('9' * int(arg))


@field_type(name="string")
def string_field(length):
    return ''.join(choice(lc_set) for i in range(length))


@field_arg(name="string")
def string_field_argument(arg):
    return int(arg)


@field_type(name="randomset")
def randomset_field(members):
    return choice(members)


@field_arg(name="randomset")
def randomset_field_argument(arg):
    return [i for i in arg.split(',')]


@field_type(name="ipv4")
def ipv4_field(arg):
    return '.'.join('%s' % randint(0, 255) for i in range(4))


@field_arg(name="date")
def date_field_argument(arg):
    args = arg_parser(arg)
    if 'before' not in args:
        raise Exception('date field is missing required argument "before"')
    if 'after' not in args:
        raise Exception('date field is missing required argument "after"')

    tformat = "%Y-%m-%d"
    before = mktime(strptime(args['before'], tformat))
    after = mktime(strptime(args['after'], tformat))

    return before, after


@field_type(name="date")
def date_field(args):
    before, after = args

    prop = random()
    ptime = before + prop * (after - before)

    return strftime("%Y-%m-%d", localtime(ptime))
