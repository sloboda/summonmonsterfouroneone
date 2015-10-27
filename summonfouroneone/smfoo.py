#!/usr/bin/env python
""" smfoo: "summon monster four one one"

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


This file has the XML subroutines for unit testing
used by webserver.py and other applications
when filtering monster.xml
to return only a subset of information.

"""

#####################################################################
#
#   for parsing out hit dice values
from summonfouroneone import RpgDataMangling

HELPTEXT = """
Type a value in the input field, then press 'search'.

Valid values are:
-- the word "help" for this helpful message.
-- names of monsters to summon
   (e.g. 'wolf' or 'dire bat')
-- names of summon monster spells
   (e.g. 'summon monster iii')
-- integers are shorthand for summon monster spells
   (e.g. a 5 is the same as  'summon monster v')
-- The integer 0 is shorthand for "all summon monster spells"
-- special qualities that a summoned monster might have
   (e.g. 'blindsense', 'dispel magic')
-- abbreviations for special qualities that a summoned monster might have
   (e.g. type 'gli' for both 'glitterdust' and 'earth glide')
-- Modifiers are added with a leading plus sign '+'
   Valid modifiers are:
   +n +normal for normal display
   +x +extended for extended display
   +g +good +celestial to apply the celestial template to some monsters
   +e +evil +infernal to apply the infernal template to some monsters
   +a +augs '+augment summoning' to apply the Augment Summoning feat to monsters

Use quotation marks to preserve white space.
"""

def display_help_text(help_format=None):
    """display the help text.

    grabs HELPTEXT from this module and displays it.

    Take a Format operator in the future for alternate output formats.
    """
    result = ""
    if help_format == "html":
        result = "<pre>"
        result = result + HELPTEXT
        result = result + "</pre>"
    elif help_format is None:
        result = HELPTEXT
    return result



def apply_augs_feat(hit_dice, hit_point):
    """first cut at apply 'augmented summoning' feat.

    The feat adds +4 to STR and +4 to CON.
    In practice, this means +2 hit_point per HD.

    Given the hit_dice and hit_point, return the modified hit_point total
    """
    result = 0
    hit_dice = int(hit_dice)  # coerce to int
    hit_point = int(hit_point)  # coerce to int
    bonus = hit_dice * 2
    result = hit_point + bonus
    return result


### define a class for a ResultsObject, then create an instance
class ResultsObject(object):
    """object to hold results from searches.

    (at least) Two types of data in this object:
    1) A list of all monsters
    2) A string of text containing any text messages.
    """
    def __init__(self):
        self.results_list = [] # holds list of monsters
        self.flag_list = [] # holds modifiers to monsters
        self.results_text = "" # holds text for display page
        # next line is flag for list or HTML table
        # standard_list means <ol><li><li></ol> type HTML list
        self.display_output = ""

    def set_display_output(self, text=""):
        """ Set either standard short list or extended table """
        self.display_output = text

    def get_display_output(self):
        """ get toggle: either standard short list or extended table """
        result = self.display_output
        return result

    def set_results_text(self, text=""):
        """ Set text to be displayed when returning a result.

        This holds text description of what the customer searched for.
        Essentially here for real time debugging.
        """
        self.results_text = text

    def get_results_text(self):
        """ get text to be displayed in returned result"""
        result = self.results_text
        return result

    def set_results_list(self, results_list):
        """ set list of monsters returned """
        self.results_list.append(results_list)

    def get_results_list(self):
        """ get list of monsters returned """
        result = self.results_list
        return result

    def zero_results_list(self):
        """ set the list of monsters to zero (empty set)"""
        self.results_list = []

    def set_modifier_flags(self, flag_list):
        """ set list of modifier flags submitted by customer query"""
        self.flag_list.append(flag_list)

    def get_modifier_flags(self):
        """ get list of modifier flags submitted by customer query"""
        result = self.flag_list
        return result

    def zero_modifier_flags(self):
        """ set the list of modifier flags to zero (empty set)"""
        self.flag_list = []



class MonsterObject(object):
    """object to hold monster data
    """
    def __init__(self):
        self.id = ""
        self.name = ""
        self.name_w_link = ""
        self.alignment = ""
        self.prd = ""
        self.size = ""
        self.hit_dice = ""
        ### plan to phase out str called sq
        self.sq = ""
        ### plan to phase in list called special_qualities
        self.special_qualities = []
        self.hit_points = 0
        self.takes_c_or_i_template = False

    def set_id(self, text=""):
        """  set the id of the monster object"""
        self.id = text

    def get_id(self):
        """  get the id of the monster object"""
        result = self.id
        return result

    def set_takes_c_or_i_template(self, my_boolean=False):
        """ set flag for C_or_i template

        Some monsters take a Celestial or Infernal template
        Some do not.
        If this monster does take the template, set a flag here.
        """
        self.takes_c_or_i_template = my_boolean

    def get_takes_c_or_i_template(self):
        """ determine if this monster takes a c_or_i template """
        result = self.takes_c_or_i_template
        return result

    def set_name(self, text=""):
        """ Set the name of the monster """
        self.name = text

    def get_name(self):
        """ get the name of the monster """
        result = self.name
        return result

    def set_sq(self, text=""):
        """ set the text of the special quality"""
        self.sq = text

    def get_sq(self):
        """ get the text of the special quality"""
        result = self.sq
        return result

    def set_special_qualities(self, results_list=None):
        """ set the list of special qualities"""
        for thing in results_list:
            if thing not in self.special_qualities: # do not add it twice
                self.special_qualities.append(thing)

    def get_special_qualities(self):
        """ get the list of special qualities"""
        result = self.special_qualities
        return result

    def zero_special_qualities(self):
        """ set the list of special qualities to empty list"""
        self.special_qualities = []

    def set_alignment(self, text=""):
        """ set alignment of the monster object"""
        self.alignment = text

    def get_alignment(self):
        """get alignment of the monster object"""
        result = self.alignment
        return result

    def set_prd(self, text=""):
        """ set the URL to the PRD

        Each monster has a URL on the Paizo Reference Document web site.
        """
        self.prd = text

    def get_prd(self):
        """get the URL to the PRD for the monster"""
        result = self.prd
        return result

    def set_size(self, text=""):
        """set size of the monster object"""
        self.size = text

    def get_size(self):
        """get size of the monster object"""
        result = self.size
        return result

    def set_hit_points(self, hit_point=0):
        """ set the hit point total"""
        self.hit_points = hit_point

    def get_hit_points(self):
        """ get the hit point total"""
        result = self.hit_points
        return result

    def set_hit_dice(self, hit_dice="1d8"):
        """ set the hit dice type : 1d8, 2d10 """
        self.hit_dice = hit_dice

    def get_hit_dice(self):
        """ get the hit dice type  """
        result = self.hit_dice
        return result

    def apply_augs_feat(self):
        """first cut at apply 'augmented summoning' feat.

        The feat adds +4 to STR and +4 to CON.
        In practice, this means +2 hit_point per HD.

        requires hit_dice and hit_point; sets the modified hit_point total
        """
        result = 0
        hit_dice = self.get_hit_dice() # get 1d8+2
        hit_dice = RpgDataMangling.parse_dice(hit_dice)[0] # get only the 1
        hit_point = self.get_hit_points()
        hit_dice = int(hit_dice)  # coerce to int
        hit_point = int(hit_point)  # coerce to int
        bonus = hit_dice * 2
        result = hit_point + bonus
        self.set_hit_points(result)

    def apply_template(self, template_name="celestial"):
        """determine if a monster may receive  either
        celestial or infernal template.

        Elementals and Demons and Archons, for example, do not.
        Apply template if monster qualifies
        """
        if self.get_takes_c_or_i_template():
            if template_name == "celestial":
                self.apply_celestial_template()
            elif template_name == "infernal":
                self.apply_infernal_template()
        else:
            pass

    def apply_celestial_template(self):
        """first cut at apply celestial_template

        The template provides a number of features
           dependent on hit dice.
        Assumption at start is that this is a string.
        It might make more sense to work with a list for the
           sq attribute,
        and convert that list into a string using the
           get_html_string() method.
        """
        sq = ""
        hit_dice = self.get_hit_dice() # get 1d8+2
        hit_dice = RpgDataMangling.parse_dice(hit_dice)[0] # get only the 1
        hit_dice = int(hit_dice)  # coerce to int
        smite = "smite evil 1/day for +%d dmg" % hit_dice
        sq_list_low = ['resist acid 5', 'resist cold 5',
                       'resist electricity 5', smite]
        sq_list_med = ['DR 5/evil', 'resist acid 10',
                       'resist cold 10', 'resist electricity 10', smite]
        sq_list_high = ['DR 10/evil', 'resist acid 15', 'resist cold 15',
                        'resist electricity 15', smite]
        if hit_dice > 0 and hit_dice < 5:
            self.set_special_qualities(sq_list_low)
        elif hit_dice > 4 and hit_dice < 11:
            self.set_special_qualities(sq_list_med)
        else:
            self.set_special_qualities(sq_list_high)

    def apply_infernal_template(self):
        """first cut at apply infernal_template

        The template provides a number of features
           dependent on hit dice.
        Assumption at start is that this is a string.
        It might make more sense to work with a list for the
           sq attribute,
        and convert that list into a string using the
           get_html_string() method.
        """
        sq = ""
        hit_dice = self.get_hit_dice() # get 1d8+2
        hit_dice = RpgDataMangling.parse_dice(hit_dice)[0] # get only the 1
        hit_dice = int(hit_dice)  # coerce to int
        smite = "smite good 1/day for +%d dmg" % hit_dice
        sq_list_low = ['resist cold 5', 'resist fire 5', smite]
        sq_list_med = ['DR 5/good', 'resist cold 10', 'resist fire 10', smite]
        sq_list_high = ['DR 10/good', 'resist cold 15',
                        'resist fire 15', smite]
        if hit_dice > 0 and hit_dice < 5:
            self.set_special_qualities(sq_list_low)
        elif hit_dice > 4 and hit_dice < 11:
            self.set_special_qualities(sq_list_med)
        else:
            self.set_special_qualities(sq_list_high)

    def set_name_w_link(self):
        """method to set a name that is a hyperlink

        Finds existing attributes  name 'eagle' and prd 'http://foobar/prd'
        sets <a href="http://foobar/prd">eagle</a>
        """
        name = self.get_name()
        prd = self.get_prd()
        result = '''<a href = "''' + prd + '''">''' + name + '</a>'
        self.name_w_link = result

    def get_name_w_link(self):
        """ get the name of the monster wrapped in a URL link"""
        result = self.name_w_link
        return result

    def get_html_string(self, monobj_attr=""):
        """return the value for monobj_attr as HTML

        MonsterObject attributes may be:
            strings such as name, or
            integers such as hit_points, or
            lists such as special_qualities

        This method returns the result as a string.
        If the attribute is empty, return the HTML entity
            for non breaking space &nbsp;
        """
        result = ""
        value = 0
        # build method call from method input
        try:
            value = getattr(self, "get_%s" % monobj_attr)()
        except AttributeError:
            value = None  #  this may be a source of problems.
            ### should watch this try/except block; may cause future errors.
        if value is None:   # Some attributes do not have values
            result = '&nbsp;'
        elif value == "":
            result = '&nbsp;'
        else:
            result = str(value)
        #  with argument monobj_attr, check if that references an internal
        #     attribute that isinstance "list".  If it does,
        #     then break the list apart and send w/o single quotes
        #     Saves some text and is arguably more readable
        if hasattr(self, monobj_attr):
            if isinstance(getattr(self, str(monobj_attr)), list):
                result = ""
                value = getattr(self, "get_%s" % monobj_attr)()
                for myvalue in sorted(value):
                    result = myvalue + ", " + result
                result = result.rstrip(', ') # remove final comma
        return result







