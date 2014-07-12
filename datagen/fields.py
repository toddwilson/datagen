from __future__ import absolute_import

from random import randint, choice, random
import sys
import os
import io
import csv
from time import strptime, mktime, strftime, localtime
from . import method_dispatch


if sys.version_info.major == 2:
    from string import lowercase
    from string import uppercase
    lset = lowercase + uppercase
elif sys.version_info.major == 3:
    from string import ascii_letters as lset


def field_type(name):
    """ Decorator for registering a new field type """

    def dec(f):
        if name in method_dispatch:
            method_dispatch[name][0] = f
        else:
            method_dispatch[name] = [f, None]
        return f

    return dec


def field_arg(name):
    """ Decorator for registering a new field type argument handler """

    def dec(f):
        if name in method_dispatch:
            method_dispatch[name][1] = f
        else:
            method_dispatch[name] = [None, f]
        return f

    return dec


def arg_parser(arg):
    arglist = [a.split('=') for a in arg.replace(' ', '').split(',')]

    args = {}
    for pack in arglist:
        if len(pack) == 1:
            args[pack[0]] = None
        else:
            args[pack[0]] = pack[1]

    return args


def datafile(name):
    path = os.path.dirname(__file__)
    fullpath = os.path.join(path, 'data', name)

    def cell(row):
        if len(row) == 1:
            return row[0]
        else:
            return row

    with io.open(fullpath, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter=';')
        data = [cell([item for item in row]) for row in reader]

    return data


firstnames = datafile('firstnames')
lastnames = datafile('lastnames')


@field_type("bool")
def bool_field(arg):
    return choice((1, 0))


@field_type("int")
def integer_field(length):
    return randint(0, length)


@field_arg("int")
def integer_field_argument(arg):
    return int('9' * int(arg))


@field_type("string")
def string_field(length):
    return ''.join(choice(lset) for i in range(length))


@field_arg("string")
def string_field_argument(arg):
    return int(arg)


@field_type("randomset")
def randomset_field(members):
    return choice(members)


@field_arg("randomset")
def randomset_field_argument(arg):
    return [i for i in arg.split(',')]


@field_type("ipv4")
def ipv4_field(arg):
    return '.'.join('%s' % randint(0, 255) for i in range(4))


@field_arg("date")
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


@field_type("date")
def date_field(args):
    before, after = args

    return strftime("%Y-%m-%d", localtime(before + random() * (after - before)))


@field_type("ssn")
def ssn_field(arg):
    return "%.3i-%.2i-%.4i" % (randint(1, 999), randint(1, 99), randint(1, 9999))


@field_type("firstname")
def firstname_field(arg):
    return choice(firstnames)


@field_type("lastname")
def lastname_field(arg):
    return choice(lastnames)
