#!/usr/bin/env python 
""" handle_form_input


This file has methods  for 
cleaning and santizing form input
used by web.py and other applications
when filtering monster.xml 
to return only a sub set of information.

"""

import re
import shlex

MAX_INPUT_CHARACTER_LENGTH=100


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
       input = str(input_string)
    except:
       print "cannot coerce to string"
    while len(input) > MAX_INPUT_CHARACTER_LENGTH:
       input = input[:MAX_INPUT_CHARACTER_LENGTH]
    return input
     

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

