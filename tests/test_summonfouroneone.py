"""test of summonfouroneone/smfoo module methods 

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

summonfouroneone is a (bad) portmanteau of
  Summon Monster 411
  or summon monster four one one
  or smfoo

The file summonfouroneone/smfoo.py contains methods
  to help with directory assistance when summoning monsters
  in the PFRPG.
"""

import os
import random
import sys
import unittest

from summonfouroneone import smfoo
from summonfouroneone import smxml
from summonfouroneone import RpgDataMangling


class summonmonsterfouroneone(unittest.TestCase):
    """ test smfoo methods """

    def setUp(self):
        """ set up goes here """
        pass

    def test_apply_celestial_template_to_eagly(self):
        """eagle takes celestial template"""
        expect = ['resist acid 5', 'resist cold 5',
                  'resist electricity 5', 'smite evil 1/day for +1 dmg']
        monobj = smfoo.MonsterObject()
        monobj.set_name("eagle")
        monobj.set_hit_dice("1d8+1")
        monobj.set_takes_c_or_i_template(True)
        monobj.apply_template("celestial")
        result = monobj.get_special_qualities()
        self.assertEqual(expect, result)

    def test_return_empty_list_for_no_special_qualities(self):
        """monster object w no special_qualities returns empty list """
        expect = []
        monobj = smfoo.MonsterObject()
        result = monobj.get_special_qualities()
        self.assertEqual(expect, result)

    def test_return_html_for_monobj_attr_full(self):
        """for a monster object attribute with a value, return html string"""
        expect = '5'
        monobj = smfoo.MonsterObject()
        monobj.set_hit_points(5)
        result = monobj.get_html_string('hit_points')
        self.assertEqual(expect, result)

    def test_return_html_for_monobj_attr_empty(self):
        """empty monster object attr returns html non-breaking space """
        expect = '&nbsp;'
        monobj = smfoo.MonsterObject()
        result = monobj.get_html_string('senses')
        self.assertEqual(expect, result)

    def test_find_hd_of_eagle(self):
        """given an eagle, return the number of hit dice the eagle has"""
        expect = 1 
        mx = smxml.smxml()
        raw_hitdice = sorted(mx.id_into_dict('101', ['hit_dice']).values())[0]
        # raw_hitdice would contain something like (1d8+2) and we want only the 1
        result = RpgDataMangling.parse_dice(raw_hitdice)[0]
        self.assertEqual(expect, result)

    def test_find_hp_of_eagle(self):
        """given an eagle, return the value for average hit points """
        expect = 5 
        mx = smxml.smxml()
        raw_hitpoints = sorted(mx.id_into_dict('101',
                                               ['hit_points']).values())[0]
        result = int(raw_hitpoints)
        self.assertEqual(expect, result)

    def test_find_hp_of_eagle_w_augs_feat(self):
        """given an eagle, apply augment summoning feat, show hit points """
        expect = 7 
        mx = smxml.smxml()
        raw_hitpoints = sorted(mx.id_into_dict('101',
                                               ['hit_points']).values())[0]
        raw_hitdice = sorted(mx.id_into_dict('101', ['hit_dice']).values())[0]
        hitdice = RpgDataMangling.parse_dice(raw_hitdice)[0]
        hitpoints = smfoo.apply_augs_feat(hitdice, raw_hitpoints)
        result = int(hitpoints)
        self.assertEqual(expect, result)

    def test_call_monster_apply_augs_feat_get_hit_points(self):
        """use monster's applyASFeat() method, match final hp """
        expect = 7 
        monobj = smfoo.MonsterObject()
        monobj.set_hit_points(5)
        monobj.set_hit_dice("1d8+1")
        monobj.apply_augs_feat()
        hitpoints = monobj.get_html_string('hit_points')
        result = int(hitpoints)
        self.assertEqual(expect, result)

    def test_find_sq_of_eagle(self):
        """find the special qualities of a eagle, no template """
        expect = '&nbsp;'
        monobj = smfoo.MonsterObject()
        result = monobj.get_html_string('sq')
        self.assertEqual(expect, result)

    def test_find_sq_of_eagle_celestial(self):
        """find the special qualities of a eagle with celestial template """
        expect = 'smite evil 1/day for +1 dmg,'
        expect = expect + ' resist electricity 5, resist cold 5, resist acid 5'
        monobj = smfoo.MonsterObject()
        monobj.set_hit_dice("1d8+1")
        monobj.apply_celestial_template()
        result = monobj.get_html_string('special_qualities')
        self.assertEqual(expect, result)

    def test_find_sq_of_eagle_infernal(self):
        """find the special qualities of a eagle with infernal template """
        expect = 'smite good 1/day for +1 dmg, resist fire 5, resist cold 5'
        monobj = smfoo.MonsterObject()
        monobj.set_hit_dice("1d8+1")
        monobj.apply_infernal_template()
        result = monobj.get_html_string('special_qualities')
        self.assertEqual(expect, result)

    def test_find_name_of_first_monobj_in_resultset(self):
        """build a results list, find name of first object in list """
        expect = 'dog, riding'
        ro = smfoo.ResultsObject()
        for term in ['dog, riding', 'eagle']:
            monobj = smfoo.MonsterObject()
            monobj.set_name(term)
            ro.set_results_list(monobj)
        ### assumption here is that with two items, the term we want
        ### is always the name of the first item
        result_object = ro.get_results_list()[0]
        result = result_object.get_name()
        self.assertEqual(expect, result)

    def test_find_name_of_second_monobj_in_resultset(self):
        """build a results list, find name of second object in list"""
        expect = 'eagle'
        ro = smfoo.ResultsObject()
        for term in ['dog, riding', 'eagle']:
            monobj = smfoo.MonsterObject()
            monobj.set_name(term)
            ro.set_results_list(monobj)
        ### assumption here is that with two items, the term we want
        ### is always the name of the second item
        result_object = ro.get_results_list()[1]
        result = result_object.get_name()
        self.assertEqual(expect, result)

    def test_build_name_w_hyperlink(self):
        """return href with name as linktext and prd link as link target"""
        expect = """<a href = "foobar">eagle</a>"""
        monobj = smfoo.MonsterObject()
        monobj.set_name('eagle')  # give object a name 
        monobj.set_prd('foobar')  # give object a link
        monobj.set_name_w_link()  # set the attribe w name and link
        result = monobj.get_name_w_link() # get attribute 
        self.assertEqual(expect, result)

    def test_display_help_text(self):
        """request for help displays help text"""
        expect = smfoo.HELPTEXT
        result = smfoo.display_help_text()
        self.assertEqual(expect, result)


if __name__ == "__main__":
    unittest.main() 
        
