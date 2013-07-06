#!/usr/bin/env python

"""rpg_data_mangling   parse text used in RPG games.

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
class rpg_data_mangling_error(Exception): pass


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
    pattern = "(\d+)d(\d+)\+?(\d+)?"
    prog = re.compile(pattern)
    try:
        results = prog.findall(dice_expression)  # findall returns a list
    except:
        raise rpg_data_mangling_error("I don't know what you are saying")
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
    pass

###########################################################
### This file can be imported.
### The following line allows the script to be called from the command line.

if __name__ == "__main__":
    main()
