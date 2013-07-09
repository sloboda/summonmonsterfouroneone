"""unit test for rpg_data_mangling.py


copyright (c) 2013  by david sloboda

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




Unit tests for methods that rearrange (mangle) role playing game data.


This file is a unit test. 
The idea behind unit testing is to call this script
and have it test a series of individual aspects of the file named in the first line.

More on python unit testing at
http://diveintopython.org/unit_testing/diving_in.html

call via
$ python tests/rt.py -v
which will call all tests/test_*.py files

"""

###########################################################
### version information goes here
### Redo for git for revision control


###########################################################
### import modules here
import unittest
import rpg_data_mangling

###########################################################
class KnownValues(unittest.TestCase):

    def setUp(self):
        ### set up defaults here
        pass


    def test_get_number_of_dice(self):
        """get the number of dice. The 2 in 2d6+3"""
        expect = 2
        result = rpg_data_mangling.parse_dice("2d6+3")[0]
        self.assertEqual(expect, result)
        

    def test_get_type_of_dice(self):
        """get the type of dice. The 6 in 2d6+3"""
        expect = 6
        result = rpg_data_mangling.parse_dice("2d6+3")[1]
        self.assertEqual(expect, result)
        

    def test_get_bonus_of_dice(self):
        """get the bonus applied to the dice roll. The 3 in 2d6+3"""
        expect = 3
        result = rpg_data_mangling.parse_dice("2d6+3")[2]
        self.assertEqual(expect, result)
        

    def test_get_big_number_of_dice(self):
        """get the number of dice. The 22 in 22d20+31"""
        expect = 22
        result = rpg_data_mangling.parse_dice("22d20+31")[0]
        self.assertEqual(expect, result)
        

    def test_get_big_type_of_dice(self):
        """get the type of dice. The 20 in 22d20+31"""
        expect = 20
        result = rpg_data_mangling.parse_dice("22d20+31")[1]
        self.assertEqual(expect, result)
        

    def test_get_big_bonus_of_dice(self):
        """get the bonus applied to the dice roll. The 31 in 22d20+31"""
        expect = 31
        result = rpg_data_mangling.parse_dice("22d20+31")[2]
        self.assertEqual(expect, result)
        

    def test_get_type_of_dice_no_bonus(self):
        """get the type of dice with no bonus. The 12 in 3d12"""
        expect = 12
        result = rpg_data_mangling.parse_dice("3d12")[1]
        self.assertEqual(expect, result)
        

    def test_get_number_of_dice_no_bonus(self):
        """get the number of dice with no bonus. The 3 in 3d12"""
        expect = 3
        result = rpg_data_mangling.parse_dice("3d12")[0]
        self.assertEqual(expect, result)
        

    def test_get_type_of_dice_no_bonus_upper(self):
        """handle D. get the type of dice with no bonus. The 8 in 4D8"""
        expect = 8
        result = rpg_data_mangling.parse_dice("4D8")[1]
        self.assertEqual(expect, result)
        

    def test_get_number_of_dice_no_bonus_upper(self):
        """handle D. get the number of dice with no bonus. The 4 in 4D8"""
        expect = 4
        result = rpg_data_mangling.parse_dice("4D8")[0]
        self.assertEqual(expect, result)
        



if __name__ == "__main__":
    unittest.main()
