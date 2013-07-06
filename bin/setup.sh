#!/usr/bin/env bash

# setup.sh
# PURPOSE
# set environment variables to include the bin and library directories 
# for the sm411 program.
#
# USAGE
# Edit this file to put the full path to smfoo in PROJECTDIR
#   then, run as follows:
# cd {whatever path you put in PROJECTDIR}
# . ./bin/setup.sh
# That source (.) command loads the environment variables 
#
# LAST MODIFIED
# Fri Jul  5 21:13:41 PDT 2013
# 
# Copyright 2013, sloboda
#
# This program is free software, and is provided "as is" 
# without warranty of any kind, express or implied, 
# to the extent permitted by applicable law.
# See the full license in the file 'COPYING'.
#
# This software includes Open Game Content.  
# See the file 'OGL' for more information.
#


# replace this with the full path to sm411 on your system
PROJECTDIR="/opt/sm/summonmonster411"

PATH=$PATH:$PROJECTDIR/bin
### python files to be imported go in directory specified by next line
PYTHONPATH=$PYTHONPATH:$PROJECTDIR/summonfouroneone

export PATH
export PYTHONPATH

# Do not put an exit statement in script, or the shell will terminate.
#exit 0

