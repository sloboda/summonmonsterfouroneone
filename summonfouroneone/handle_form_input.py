#!/usr/bin/env python
""" handle_form_input

copyright (c) 2015  by david sloboda

This file is part of summonmonsterfouroneone.

summonmonsterfouroneone is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

summonmonsterfouroneone is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with summonmonsterfouroneone in the file COPYING.
If not, see <http://www.gnu.org/licenses/>

This file has methods for
cleaning and santizing form input
used by webserver.py and other applications
when filtering monster.xml
to return only a subset of information.

"""

import re
import shlex
import sys

MAX_INPUT_CHARACTER_LENGTH = 100

def check_is_input_cry_for_help(form_input):
    """check to see if form input is a request for help

    return True if it is a cry for help,
    otherwise return False
    """
    result = False
    help_terms = ["help", "--help", "+help", "usage", "+usage"]
    if form_input in help_terms:
        result = True
    return result

def split_input_keep_quotes(form_input):
    """split input sent to form. preserve 'quoted whitespace'

    return a list
    """
    result = []
    result = shlex.split(form_input)
    return result

def check_input_length(input_string):
    """check input length of input_string

    returns string sliced to MAX_INPUT_CHARACTER_LENGTH characters.
    """
    result = ""
    try:
        result = str(input_string)
    except ValueError:
        print "cannot coerce to string"
        sys.exit(2)
    while len(result) > MAX_INPUT_CHARACTER_LENGTH:
        result = result[:MAX_INPUT_CHARACTER_LENGTH]
    return result


def scrub_form_input(input_string):
    """check input_string for bad characters we do not want.

    Remove them.
    returns string
    """
    result = ""
    #  remove backslash  \
    pattern = "\\\\"
    prog = re.compile(pattern)
    input_string = re.sub(prog, "", input_string)

    # remove percentage sign %
    pattern = '%'
    prog = re.compile(pattern)
    input_string = re.sub(prog, "", input_string)

    # remove dollar sign $
    pattern = '\$'
    prog = re.compile(pattern)
    input_string = re.sub(prog, "", input_string)

    # remove semi colon ;
    pattern = '\;'
    prog = re.compile(pattern)
    input_string = re.sub(prog, "", input_string)

    result = input_string
    return result

