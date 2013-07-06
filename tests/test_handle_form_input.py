"""test of handle form input methods

handle_form_input.py contains the methods and functions used to 
scrub form input
and parse the form input
for Summon Monster Four One One (sm411).
"""



import os
import random
import sys
import unittest


from summonfouroneone import handle_form_input


class form_input_summon_monster_four_one_one(unittest.TestCase):
    """ test smxml """

    def setUp(self):
        """ set up goes here """
        pass


    def test_crop_101_input(self):
        """input of 101 characters is cropped to 100 characters """
        #  expect a string 100 characters in length
        expect = 'abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy01234'
        #  send a string 101 characters in length
        form_input = 'abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy012345'
        result = handle_form_input.check_input_length(form_input)
        self.assertEqual(expect, result)


    def test_crop_105_input(self):
        """input of 105 characters is cropped to 100 characters """
        #  expect a string 100 characters in length
        expect = 'abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy01234'
        #  send a string 105 characters in length
        form_input = 'abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy0123456789'
        result = handle_form_input.check_input_length(form_input)
        self.assertEqual(expect, result)


    def test_do_not_crop_safe_input(self):
        """input of 100 characters is untouched """
        #  expect a string 100 characters in length
        expect = 'abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy01234'
        #  send a string 105 characters in length
        form_input = 'abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy0123456789abcdefghijklmnopqrstuvwxy01234'
        result = handle_form_input.check_input_length(form_input)
        self.assertEqual(expect, result)


    def test_scrub_semicolon(self):
        """semicolon within input is removed """
        expect = 'demon'
        form_input = 'de;mon'
        result = handle_form_input.scrub_form_input(form_input)
        self.assertEqual(expect, result)


    def test_scrub_backslash(self):
        """backslash within input is removed """
        expect = 'demon'
        form_input = 'de\mon'
        result = handle_form_input.scrub_form_input(form_input)
        self.assertEqual(expect, result)


    def test_scrub_percentage_sign(self):
        """percentage_sign within input is removed """
        expect = 'bear'
        form_input = 'be%ar'
        result = handle_form_input.scrub_form_input(form_input)
        self.assertEqual(expect, result)


    def test_scrub_dollar_sign(self):
        """dollar sign within input is removed """
        expect = 'dolphin'
        form_input = 'dolphin$'
        result = handle_form_input.scrub_form_input(form_input)
        self.assertEqual(expect, result)


    def test_split_input_on_quoted_whitespace(self):
        """ input 'in quotes' is preserved """
        expect = ['0', 'dire bear',  '1', '+good', '+augs', 'succubus', 'elemental, fire', '4']
        form_input = "0 'dire bear' 1 +good +augs succubus 'elemental, fire' 4"
        result = handle_form_input.split_input_keep_quotes(form_input)
        self.assertEqual(expect, result)
        

    def test_request_for_help_is_true(self):
        """ input of single term 'help' returns True """
        expect = True
        form_input = "help"
        result = handle_form_input.check_is_input_cry_for_help(form_input)
        self.assertEqual(expect, result)
        

    def test_request_for_plushelp_is_true(self):
        """ input of single term '+help' returns True """
        expect = True
        form_input = "+help"
        result = handle_form_input.check_is_input_cry_for_help(form_input)
        self.assertEqual(expect, result)
        

    def test_request_for_help_is_false(self):
        """ input of single term 'holp' returns False """
        expect = False
        form_input = "holp"
        result = handle_form_input.check_is_input_cry_for_help(form_input)
        self.assertEqual(expect, result)
        




if __name__ == "__main__":
    unittest.main() 
        
