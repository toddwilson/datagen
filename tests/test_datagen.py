from pytest import raises

from datagen import main


def test_demands_required_arguments():
    with raises(SystemExit):
        main([])


def _run_main(tmpdir, schema, args):
    test_tmpdir = tmpdir.mkdir("testdata")
    schemafile = test_tmpdir.join("schema.txt")
    schemafile.write(schema)
    outfile = test_tmpdir.join("result.txt")
    args += ['-s', schemafile.strpath, outfile.strpath]
    main(args)
    with open(outfile.strpath) as outfile_obj:
        result = outfile_obj.read()
    return result


SCHEMA_FROM_README = """
	#name      type[argument]
	id         int[6]
	first      firstname
	last       lastname
	email      email
	dob        date[after=1945-01-01, before=2001-01-01]
	password   string[8]
	is_active  bool
	language   randomset[python,ruby,go,java,c,js,brainfuck]
    """


def test_as_in_readme(tmpdir):
    # import pytest; pytest.set_trace()
    args = ['-n', '5', '--with-header']
    result = _run_main(tmpdir, SCHEMA_FROM_README, args)
    assert result.count('|') == 42


def test_without_headers(tmpdir):
    args = ['-n', '5']
    result = _run_main(tmpdir, SCHEMA_FROM_README, args)
    assert result.count('|') == 35


def test_delimeter(tmpdir):
    args = ['-n', '5', '--with-header', '-d', ',']
    result = _run_main(tmpdir, SCHEMA_FROM_README, args)
    assert result.count(',') == 42
    assert result.count('|') == 0
