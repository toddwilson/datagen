datagen: Make sh[2] up
======================

Datagen helps you create sample delimited data using a simple schema format.
It runs on Python 2.6-3.4 and *particularly well* on PyPy.

Usage
-----

    usage: datagen [-h] [-d DELIMITER] [--with-header] -n NUM_ROWS -s SCHEMA [output]


**1. Create a schema file**

::

    $ cat > schema.txt <<EOL
	#name		type[argument]
	id			int[6]
	first		firstname
	last		lastname
	email		email
	dob         date[after=1945-01-01, before=2001-01-01]
	password	string[8]
	is_active	bool
	language	randomset[python,ruby,go,java,c,js,brainfuck]
    EOL

**2. Make data**

::

	$ datagen -s schema.txt -n 5 --with-header
	id|first|last|email|dob|password|is_active|language
	238476|Velma|Medrano|sxLYZTnPf@ACLoxOVjUu.edu|1948-01-12|KmAcXnnS|1|python
	202490|Kathy|Wellman|pAXx@MQcPrkMdNMcZa.com|1960-11-12|BwtZnRUN|1|java
	905703|Fern|Odell|iCQ@KtN.mil|1972-12-12|ipVagvEB|0|c
	130211|Khadijah|Sheffield|KBPf@ibR.edu|1961-02-02|ijAVDWUY|0|java
	643257|Patricia|Cummings|vaZqWhl@YcVvZXx.int|1960-05-01|GJdImZaw|0|ruby

**3. Actually start working on what you should be working on**


Types
-----

**bool**: 1 or 0 randomly.

**int[length]**: A random unsigned integer.

Params:

* length: max-length

Example::

	number    numberint[3]

	509
	49
	783


**incrementing_int**: An automatically incrementing unsigned integer.

Example::

    id    incrementing_int



**string[length]**: A random case-insensitive string.

Params:

* length: max-length



