#/usr/bin/env python
import argparse
import re
import csv
import sys
import fields

re_parse_type = re.compile('(.*)\[(.*)\]')
re_parse_file = re.compile('([a-zA-Z_0-9]+)\s+([a-zA-Z0-9_]+\[?.*\]?)')


def parse_method(fstr):
    match = re_parse_type.match(fstr)

    if match is not None:
        method_name, method_arg_str = match.groups()
    else:
        method_name = fstr.strip()
        method_arg_str = None

    method, arg_handler = fields.method_dispatch[method_name.lower()]

    if arg_handler is None:
        return method, None
    else:
        return method, arg_handler(method_arg_str)


def read_schema_file(path):
    names = []
    fieldtypes = []
    f = open(path, 'r')

    n = 1

    for line in f.readlines():
        line = line.strip()
        match = re_parse_file.match(line)

        if match is None:
            if line == '':
                continue
            else:
                raise Exception('Invalid field declaration at line #%s: `%s`' % (n, line))

        name, method = match.groups()
        names.append(name)
        fieldtypes.append(parse_method(method))

    f.close()

    return names, fieldtypes


def field_type(**kwargs):
    """ Decorator for registering a new field type """

    name = kwargs.pop('name')

    def dec(f):
        if name in fields.method_dispatch:
            fields.method_dispatch[name][0] = f
        else:
            fields.method_dispatch[name] = [f, None]
        return f

    return dec


def field_arg(**kwargs):
    """ Decorator for registering a new field type argument handler """

    name = kwargs.pop('name')

    def dec(f):
        if name in fields.method_dispatch:
            fields.method_dispatch[name][1] = f
        else:
            fields.method_dispatch[name] = [None, f]
        return f

    return dec


def main():
    parser = argparse.ArgumentParser(description='Generate dummy data')
    parser.add_argument('-d', '--delimiter', required=False, help='Delimter to use. Default is |')
    parser.add_argument('--with-header', required=False, action='store_true', help='Write column headers as first row')
    parser.add_argument('-n', '--num-rows', required=True, help='Number of rows to write')
    parser.add_argument('-s', '--schema', required=True, help='Schema file to load')
    parser.add_argument('output', nargs='?', help='Path to write to (STDOUT if not specified')

    args = parser.parse_args()

    if args.output is None:
        output = sys.stdout
    else:
        output = open(args.output, 'w')

    delimiter = '|'
    if args.delimiter:
        delimiter = args.delimiter

    names, fieldtypes = read_schema_file(args.schema)

    writer = csv.writer(output, delimiter=delimiter)

    num_rows = int(args.num_rows)
    current_row = 0

    if args.with_header:
        writer.writerow(names)

    while current_row < num_rows:
        writer.writerow([str(method(argument)) for method, argument in fieldtypes])
        current_row += 1


if __name__ == '__main__':
    main()
