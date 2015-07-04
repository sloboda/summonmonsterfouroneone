#!/usr/bin/env bash

# setup.sh
# PURPOSE
# set environment variables to include the bin and library directories 
# for summonmonsterfouroneone.
#
# USAGE
# Edit this file to put the full path to 
#   the base summonmonsterfouroneone directory in PROJECTDIR
#   then, run as follows:
# cd {whatever path you put in PROJECTDIR}
# . ./bin/setup.sh
# That source (.) command loads the environment variables 
#
# LAST MODIFIED
# Fri Jul  5 21:13:41 PDT 2013
# 
# 
# copyright (c) 2013  by david sloboda
# 
# This file is part of summonmonsterfouroneone.
# 
# summonmonsterfouroneone is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# summonmonsterfouroneone is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with summonmonsterfouroneone in the file COPYING.  
# If not, see <http://www.gnu.org/licenses/>.



# replace this with the full path 
#    to summonmonsterfouroneone on your system
PROJECTDIR="/opt/sm/summonmonsterfouroneone"

PATH=$PATH:$PROJECTDIR/bin
### python files to be imported go in directory specified by next line
PYTHONPATH=$PYTHONPATH:$PROJECTDIR/summonfouroneone

export PATH
export PYTHONPATH

# Do not put an exit statement in script, or the shell will terminate.
#exit 0

