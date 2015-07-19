"""test of smxml Summon Monster XML methods and functions

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





smxml.py contains the methods and functions used to 
query xml data for Summon Monster Four One One (sm411).
"""



import os
import random
import sys
import unittest


from summonfouroneone import smxml


class summon_monster_four_one_one(unittest.TestCase):
    """ test smxml """

    def setUp(self):
        """ set up goes here """
        pass


    def test_find_all_id_attributes_for_monster_elements_on_sm1_sl(self):
        """given a 1, find all ID values for monster elements on SM1 spell list"""
        expect = ['100', '101', '102', '103', '104', '105', '106', '107'] 
        mx = smxml.smxml()
        result = mx.search_for_id_attributes(1)
        self.assertEqual(expect, result)


    def test_find_all_id_attributes_for_monster_elements_on_sm2_sl(self):
        """given a 2, find all ID values for monster elements on SM2 spell list"""
        expect = ['200', '201', '202', '203', '204', '205', '206', '207', '208', '209', 
                  '210', '211', '212', '213', '214']
        mx = smxml.smxml()
        result = mx.search_for_id_attributes(2)
        self.assertEqual(expect, result)


    def test_find_all_id_attributes_for_monster_elements_on_sm3_sl(self):
        """given a 3, find all ID values for monster elements on SM3 spell list"""
        expect = ['300', '301', '302', '303', '304', '305', '306', '307', '308', '309', 
                  '310', '311', '312', '313', '314', ]
        mx = smxml.smxml()
        result = mx.search_for_id_attributes(3)
        self.assertEqual(expect, result)


    def test_find_all_id_attributes_for_monster_elements_on_sm4_sl(self):
        """given a 4, find all ID values for monster elements on SM4 spell list"""
        expect = ['400', '401', '402', '403', '404', '405', '406', '407', '408', '409', 
                  '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', 
                  '420', '421', '422', '423', '424', '425', '426', '427', ]
        mx = smxml.smxml()
        result = mx.search_for_id_attributes(4)
        self.assertEqual(expect, result)


    def test_find_all_id_attributes_for_monster_elements_on_sm5_sl(self):
        """given a 5, find all ID values for monster elements on SM5 spell list"""
        expect = ['500', '501', '502', '503', '504', '505', '506', '507', '508', '509', 
                  '510', '511', '512', '513', '514', ]
        mx = smxml.smxml()
        result = mx.search_for_id_attributes(5)
        self.assertEqual(expect, result)


    def test_find_all_id_attributes_for_monster_elements_on_sm6_sl(self):
        """given a 6, find all ID values for monster elements on SM6 spell list"""
        expect = ['600', '601', '602', '603', '604', '605', '606', '607', '608', '609', 
                  '610', '611', '612', '613', '614', ]
        mx = smxml.smxml()
        result = mx.search_for_id_attributes(6)
        self.assertEqual(expect, result)


    def test_find_all_id_attributes_for_all_monster_elements_on_all_sl(self):
        self.maxDiff = None
        """given a 0, find all ID values for all monster elements on all spell lists"""
        expect = ['100', '101', '102', '103', '104', '105', '106', '107', 
                  '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', 
                  '210', '211', '212', '213', '214',
                  '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', 
                  '310', '311', '312', '313', '314',
                  '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', 
                  '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', 
                  '420', '421', '422', '423', '424', '425', '426', '427',
                  '500', '501', '502', '503', '504', '505', '506', '507', '508', '509', 
                  '510', '511', '512', '513', '514', 
                  '600', '601', '602', '603', '604', '605', '606', '607', '608', '609',
                  '610', '611', '612', '613', '614',
                  '700', '701', '702', '703', '704', '705', '706', '707', '708', '709',
                  '710', '711', '712', '713', 
                  '800', '801', '802', '803', '804', '805', 
                  '900', '901', '902', '903', '904', '905']
        mx = smxml.smxml()
        result = mx.search_for_id_attributes(0)
        self.assertEqual(expect, result)


    def test_return_elements_for_id_613(self):
        """given monster element with attribute id=613, return child elements"""
        expect = [[{'name': 'succubus (demon)'}, {'prd': 'http://paizo.com/pathfinderRPG/prd/monsters/demon.html#demon-succubus'}, {'alignment': 'CE'}, {'size': 'M'}]]
        mx = smxml.smxml()
        result = mx.id_attributes_into_element_values(['613'])
        self.assertEqual(expect, result)


    def test_find_id_value_for_monster_name(self):
        """given the name Eagle, find id 101 """
        expect = ['101'] 
        mx = smxml.smxml()
        result = mx.search_for_monster_name("Eagle")
        self.assertEqual(expect, result)


    def test_ignore_case_when_id_value_for_monster_name(self):
        """given the name eaGLe, find id 101 """
        expect = ['101'] 
        mx = smxml.smxml()
        result = mx.search_for_monster_name("eaGLe")
        self.assertEqual(expect, result)


    def test_on_partial_name_find_a_match(self):
        """given partial input eagl, find id 101 """
        expect = ['101'] 
        mx = smxml.smxml()
        result = mx.search_for_monster_name("eagl")
        self.assertEqual(expect, result)


    def test_given_id_return_dict_keys_simple_eagle(self):
        """sorted id2dict keys on eagle id 101 """
        expect = ['alignment', 'name', 'prd', 'size']
        mx = smxml.smxml()
        result = sorted(mx.id_into_dict('301', ['name','prd','alignment','size']).keys())
        self.assertEqual(expect, result)


    def test_given_id_return_dict_keys_complicated_dretch(self):
        """sorted id2dict keys on dretch id 308 with subelements """
        expect = ['alignment', 'name', 'prd', 'size', 'special_qualities']
        mx = smxml.smxml()
        result = sorted(mx.id_into_dict('308', ['name','prd','alignment','size','special_qualities']).keys())
        self.assertEqual(expect, result)


    def test_given_id_return_dict_values_complicated_dretch(self):
        """sorted id2dict values on dretch id 308 subelements  'special_qualities' """
        expect = ['DR 5/cold iron or good', 'cause fear (DC11) 1/day', 'immune electricity', 
           'immune poison', 'resist acid 10', 'resist cold 10', 
           'resist fire 10', 'stinking cloud (DC13) 1/day']
        mx = smxml.smxml()
        result = sorted(mx.id_into_dict('308', ['name','prd','alignment','size','special_qualities'])['special_qualities'])
        self.assertEqual(expect, result)


    def test_given_id_and_key_not_in_element_pass(self):
        """pass on nonexistent  key 'foobar' on dretch id 308 with subelements """
        expect = ['alignment', 'name', 'prd', 'size', 'special_qualities']
        mx = smxml.smxml()
        result = sorted(mx.id_into_dict('308', ['name','prd','alignment','foobar', 'size','special_qualities']).keys())
        self.assertEqual(expect, result)


    def test_find_id_value_for_monster_sq_term(self):
        """given the sq_term blindsense, find id 307, 313, 705"""
        expect = ['307', '313', '705'] 
        mx = smxml.smxml()
        result = mx.search_for_monster_sq("blindsense")
        self.assertEqual(expect, result)


    def test_ignore_case_when_id_value_for_monster_sq_term(self):
        """given the sq_term bliNDSEnse, find id 307, 313, 705 """
        expect = ['307', '313', '705'] 
        mx = smxml.smxml()
        result = mx.search_for_monster_sq("bliNDSEnse")
        self.assertEqual(expect, result)


    def test_on_partial_sq_term_find_a_match(self):
        """given partial input blindsens, find id 307, 313, 705 """
        expect = ['307', '313', '705'] 
        mx = smxml.smxml()
        result = mx.search_for_monster_sq("blindsens")
        self.assertEqual(expect, result)


    def test_monster_should_take_c_or_i_template(self):
        """'dog, riding' should  take a celestial or infernal template"""
        expect = True
        mx = smxml.smxml()
        result = mx.monster_takes_c_or_i_template(['100'])
        self.assertEqual(expect, result)


    def test_monster_should_not_take_c_or_i_template(self):
        """demon (succubus) should NOT take a celestial or infernal template"""
        expect = False
        mx = smxml.smxml()
        result = mx.monster_takes_c_or_i_template(['610'])
        self.assertEqual(expect, result)




if __name__ == "__main__":
    unittest.main() 
        
