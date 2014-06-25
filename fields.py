from datagen import field_type, field_arg
from random import randint, choice
from string import lowercase as lc_set

method_dispatch = {}


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
