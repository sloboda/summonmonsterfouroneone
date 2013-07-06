#!/usr/bin/env python 
""" smfoo: "summon monster four one one"



This file has the XML subroutines for unit testing
used by web.py and other applications
when filtering monster.xml 
to return only a sub set of information.

"""

#####################################################################
#  for xml searching
#
from lxml import etree
#
#####################################################################
#
#   for dynamic on the fly method call
import sys
#####################################################################
#
#   for parsing out hit dice values
from summonfouroneone import rpg_data_mangling

help_text="""
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
-- Modifiers are added with a leading plus sign '+'
   Valid modifiers are:
   +n +normal for normal display
   +x +extended for extended display
   +g +good +celestial to apply the celestial template to some monsters
   +e +evil +infernal to apply the celestial template to some monsters
   +a +augs '+augment summoning' to apply the Augment Summoning feat to monsters

Use quotation marks to preserve white space.
"""

def display_help_text(format=None):
    """display the help text.

    grabs help_text from this module and displays it.

    Take a Format operator in the future for alternate output formats.
    """
    result = ""
    if format == "html":
       result = "<pre>"
       result = result + help_text
       result = result + "</pre>"
    elif format is None:
       result = help_text
    return result



def apply_augs_feat(hd, hp):
    """first cut at apply 'augmented summoning' feat.

    The feat adds +4 to STR and +4 to CON.
    In practice, this means +2 hp per HD.

    Given the hd and hp, return the modified hp total
    """
    result = 0 
    hd = int(hd)  # coerce to int
    hp = int(hp)  # coerce to int
    bonus = hd * 2
    result = hp + bonus
    return result


### define a class for a results_object, then create an instance
class results_object(object):
    """object to hold results from searches.

    (at least) Two types of data in this object: 
    1) A list of all monsters
    2) A string of text containing any text messages.
    """
    def __init__(self):
        self.results_list = [] # holds list of monsters
        self.flag_list = [] # holds modifiers to monsters
        self.results_text = "" # holds text for display page
        """next line is flag for list or HTML table
        standard_list means <ol><li><li></ol> type HTML list
        """
        self.display_output = "" 


    def set_display_output(self, text=""):
        self.display_output = text


    def get_display_output(self):
        result = self.display_output
        return result 


    def set_results_text(self, text=""):
        self.results_text = text


    def get_results_text(self):
        result = self.results_text
        return result 


    def set_results_list(self, results_list=[]):
        self.results_list.append(results_list)

   
    def get_results_list(self):
        result = self.results_list
        return result


    def zero_results_list(self):
        self.results_list=[]


    def set_modifier_flags(self, flag_list=[]):
        self.flag_list.append(flag_list)

   
    def get_modifier_flags(self):
        result = self.flag_list
        return result


    def zero_modifier_flags(self):
        self.flag_list=[]




class monster_object(object):
    """object to hold monster data
    """ 
    def __init__(self):
        self.name = ""
        self.name_w_link = ""
        self.alignment = ""
        self.prd = ""
        self.size = ""
        self.hit_dice = ""
        self.sq = ""
        self.hit_points = 0


    def set_name(self, text=""): 
        self.name = text


    def get_name(self):
        result = self.name
        return result


    def set_sq(self, text=""): 
        self.sq = text


    def set_special_qualities(self, text=""): 
        self.sq = text


    def get_sq(self):
        result = self.sq
        return result


    def set_alignment(self, text=""): 
        self.alignment = text


    def get_alignment(self):
        result = self.alignment
        return result


    def set_prd(self, text=""): 
        self.prd = text


    def get_prd(self):
        result = self.prd
        return result


    def set_size(self, text=""): 
        self.size = text


    def get_size(self):
        result = self.size
        return result


    def set_hit_points(self, hp=0): 
        self.hit_points = hp


    def get_hit_points(self):
        result = self.hit_points
        return result


    def set_hit_dice(self, hd="1d8"): 
        self.hit_dice = hd


    def get_hit_dice(self):
        result = self.hit_dice
        return result


    def apply_augs_feat(self):
        """first cut at apply 'augmented summoning' feat.

        The feat adds +4 to STR and +4 to CON.
        In practice, this means +2 hp per HD.

        requires hd and hp; sets the modified hp total
        """
        result = 0 
        hd = self.get_hit_dice() # get 1d8+2
        hd = rpg_data_mangling.parse_dice(hd)[0] # get only the 1
        hp = self.get_hit_points()
        hd = int(hd)  # coerce to int
        hp = int(hp)  # coerce to int
        bonus = hd * 2
        result = hp + bonus
        self.set_hit_points(result)


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
        sq =""
        hd = self.get_hit_dice() # get 1d8+2
        hd = rpg_data_mangling.parse_dice(hd)[0] # get only the 1
        hd = int(hd)  # coerce to int
        if hd > 0 and hd < 5:
            sq = 'DR 5/evil'
        self.set_sq(sq)


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
        sq =""
        hd = self.get_hit_dice() # get 1d8+2
        hd = rpg_data_mangling.parse_dice(hd)[0] # get only the 1
        hd = int(hd)  # coerce to int
        sq_list = ['DR 5/good', 'resist fire 5']
        if hd > 0 and hd < 5:
            sq = sq_list # ? assign list to string, what happens?
        self.set_sq(sq)


    def set_name_w_link(self):
        """method to set a name that is a hyperlink

        Finds existing attributes  name 'eagle' and prd 'http://foobar/prd'
        sets <a href="http://foobar/prd">eagle</a>
        """
        name = self.get_name()
        prd = self.get_prd()
        result = '''<a href="''' + prd + '''">''' + name + '</a>'
        self.name_w_link = result


    def get_name_w_link(self):
        result = self.name_w_link
        return result


    def get_html_string(self, monobj_attr=""):
        """return the value for monobj_attr as HTML

        monster_object attributes may be:
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
#        value = getattr(sys.modules[__name__], "get_%s" % monobj_attr)()
        try:
            value = getattr(self,"get_%s" % monobj_attr)()
        except AttributeError:
            value = None  #  this may be a source of problems.
            ### should watch this try/except block; may cause future errors.
        if value is None:   # Some attributes do not exist
            result = '&nbsp;'
        elif value == "":   # Some exist and are empty ('') at the start
            result = '&nbsp;'
        else:
            result = str(value)
        return result 



class smxml:
    def setup_xml(self):
        ### specify path to xml file
        xmlfile = "./OGL/monsters.xml"
        t = etree.parse(xmlfile)
        return t


    def search_for_monster_name(self, monster_name="Eagle"):  
        """search xml for a monster name

        The contains(text, searchterm) method in the lxml call 
              allows for input like "dem" to match "demon"

        Returns a list of id values.  
        Each id value provides a single match 
          on an attribute "id" in a monster element in the XML file.
        """
        result = []
        smxl = smxml()
        t = smxl.setup_xml()
        monster_name = monster_name.lower()
        mypathval="""./monster/name[contains(text(), '""" + str(monster_name) +"""') ]/.."""
        for m in t.xpath(mypathval):
             mid = m.get("id")
             result.append(mid)
        return result


    def search_for_id_attributes(self, searchterm):
        result = []
        smxl = smxml()
        t = smxl.setup_xml()
        mdict={}
        elements = ["name","prd","alignment","size"]
        """ nine summon monster spells, nine integers expected

        "zero" makes a nice shorthand way of referencing the set [1-9]
        """
        expected_digits = [1 ,2, 3, 4, 5, 6, 7, 8, 9]
        try:
           int(searchterm)
        except:
           fail_text="this search method expects an integer."
           result.append(fail_text)
           return result
        if int(searchterm) in expected_digits: 
            summon_monster_integer = searchterm
            mypathval="./monster/summon_monster_integer_list[text()='" + str(summon_monster_integer) + "']/.."
            for m in t.xpath(mypathval):
                 mid = m.get("id")
                 result.append(mid)
        elif int(searchterm) == 0:  # search everything on 0 
            for i in expected_digits:
                summon_monster_integer = i
                mypathval="./monster/summon_monster_integer_list[text()='" + str(summon_monster_integer) + "']/.."
                for m in t.xpath(mypathval):
                     mid = m.get("id")
                     result.append(mid)
        else:
            pass
        return result


    def id_attributes_into_element_values(self, mylistofID=['100']):
        """turn id_attributes_into_element_values

        Expects ['100', '101']
        Searches XML file for all elements in list
        """
        result=[]
        mdict={}
        elements = ["name","prd","alignment","size"]
        smxl = smxml()
        t = smxl.setup_xml()
        for mid in mylistofID:
            mysubpath= "./monster[@id='" + str(mid) + "']"
            for mvalue in t.xpath(mysubpath):
                internal_list=[]
                for e in elements:
                    mdict[e] = mvalue.find(e).text
                    internal_list.append({e: mdict[e] })
                result.append(internal_list)
        return result


    def id_into_dict(self, my_id='100', keys=['name','prd']):
        """turn id into a dictionary of values

        Expects an id like '101'
        and a list of keys for the dictionary

        Returns a dictionary
        
        subelement_list is a list of elements that have text in their subelements, not of themselves.
        """
        result={}
        subelement_list = ['special_qualities']
        smxl = smxml()  # set up xml object
        t = smxl.setup_xml()  # attach it to our xml file
        mysubpath= "./monster[@id='" + str(my_id) + "']"
        for mvalue in t.xpath(mysubpath):
                internal_list=[]
                for k in keys:
                    if k in subelement_list:
                        mylist =[]
                        for subele in mvalue.find(k).getchildren():
                             mylist.append(subele.text)
                        result[k] = mylist
                    else:
                        if mvalue.find(k) is not None:
                            result[k] = mvalue.find(k).text
                        else:
                            pass # we've been passed a key that does not exist
        return result







