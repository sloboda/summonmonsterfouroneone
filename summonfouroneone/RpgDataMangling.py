#!/usr/bin/env python

"""rpgDataMangling   parse text used in RPG games.

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





At present, I'm not completely sure of all the parsing
that will be required from this module.
It may also be that the types of data increase.

This module is a first cut.
"""


###########################################################
### import modules here
import re

###########################################################
### define exceptions
class RpgDataManglingError(Exception):
    """ Error for handling RPG Data

    Role Playing Games make use of their own unique strings
    and data structures.
    """
    pass


###########################################################
### define other methods here

def parse_dice(dice_expression="2d6+3"):
    """parse a dice expression like 2d6+3 and return a list

    RPG notation is to use 2d6+3
        to represent the number of dice (here, 2)
        the number of sides on each die (here, 6)
        and a bonus number added to the 2d6 total (here,  3)

    This method returns a list of integers [2, 6, 3]

    """
    result = []
    dice_expression = dice_expression.lower() # turn D into d
    pattern = r"(\d+)d(\d+)\+?(\d+)?"
    prog = re.compile(pattern)
    try:
        results = prog.findall(dice_expression)  # findall returns a list
    except:
        raise RpgDataManglingError("I don't know what you are saying")
    number_of_dice = int(results[0][0])
    type_of_dice = int(results[0][1])
    result.append(number_of_dice)
    result.append(type_of_dice)
    ### not every expression has a bonus
    if results[0][2]:
        bonus_added_to_dice = int(results[0][2])
        result.append(bonus_added_to_dice)
    return result


###########################################################
### define main here
def main():
    """ where it all goes down"""
    pass

###########################################################
### This file can be imported.
### The following line allows the script to be called from the command line.

if __name__ == "__main__":
    main()
