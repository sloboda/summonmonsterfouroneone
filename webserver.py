""" webserver.py 

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
If not, see <http://www.gnu.org/licenses/>.





PURPOSE:
run a webserver that takes user input and returns useful output
   about summoned monsters.

minimalist web server provided by web.py module

"""

import re
import shlex
import web

from web import form


#####################################################################
#  for xml searching
#
from lxml import etree
"""next import breaks out XML search routines into a separate file
   for ease in unit testing.
"""
from summonfouroneone import smxml   


### routines to check user input for sanity (sane characters only)
from summonfouroneone import handle_form_input

### treat the monsters as objects with methods and attributes
from summonfouroneone import smfoo

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form( 
    form.Textbox("searchfield", 
        form.notnull, 
        description="input: help, 0 to 9, 'dire wolf', blindSENSE, +a, +good ",
        size="60",
        maxlength="100"
        ),
    form.Button("Submit a SumMon411 search!")
    ) 


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



ro = results_object()   


def check_for_synonyms(search_term):
    """There will be a better way of doing this... one day...
    """
    result = ""
    terms = {}
    terms[0] = ["all"]
    terms[1] = ["sm1", "smi", "msi", "ms1", "summon monster i",  "summon monster 1", "monster summoning i", "monster summoning 1", "one"]
    terms[2] = ["sm2", "smii", "msii", "ms2", "summon monster ii",  "summon monster 2", "monster summoning ii", "monster summoning 2", "two" ]
    terms[3] = ["sm3", "smiii", "msiii", "ms3", "summon monster iii",  "summon monster 3", "monster summoning iii", "monster summoning 3", "three"]
    terms[4] = ["sm4", "smiv", "msiv", "ms4", "summon monster iv",  "summon monster 4", "monster summoning iv", "monster summoning 4", "four"]
    terms[5] = ["sm5", "smv", "msv", "ms5", "summon monster v",  "summon monster 5", "monster summoning v", "monster summoning 5", "five"]
    for res in terms.keys():
         if search_term.lower() in terms.values()[res]:
              result = res
              break
         else:
              result= search_term
    return result
        

def check_if_modifier(input_value):
    """determine if input starts with a plus sign 

    modifers like +good +celestial +augs start with plus sign
    and modify other terms.

    returns either (yes, modifier_without_plus_sign)
    or
    (no, input_value)
    """
    result = ()
    pattern = "^\+"
    prog = re.compile(pattern)
    match_result = prog.search(input_value)
    if match_result:
        return_value = re.sub(pattern, '', input_value)
        result = ("yes", return_value)
    else:
        result = ("no", input_value)
    return result


def handle_modifier(input):
    """handle any modifiers thrown into the search field.

    A modifier starts with a plus sign
    example:   +good
    example:   +infernal

    return the text associated with the input.
    """
    result = ""
    global ro
    augment_summoning_terms = ["augs", "augment_summoning", "augment summoning", "a"] 
    celestial_terms = ["good", "celestial", "g", "gd"] 
    infernal_terms = ["evil", "infernal", "e", "ev"] 
    extended_display_terms = ["extend", "ext", "ex", "x"] 
    list_display_terms = ["normal", "list", "n"] 
    input = input.lower()
    if input in augment_summoning_terms:
         result="The Augment Summoning feat gives +4 to STR and + to CON for each summoned creature. "
    ##### set [celestial or infernal] flag once only.  Use first flag set  ####
    if "celestial" not in ro.get_modifier_flags()  and "infernal" not in ro.get_modifier_flags(): 
        if input in celestial_terms:
                 ro.zero_modifier_flags()
                 ro.set_modifier_flags("celestial")
                 result="Summoned creatures with the Celestial template smite evil. "
        if input in infernal_terms:
                 ro.zero_modifier_flags()
                 ro.set_modifier_flags("infernal")
                 result="Summoned creatures with the Infernal template smite good. "
    ##### set display flag once only.  Use standard unless flag set  ####
    if input in extended_display_terms:
         result="You chose the extended display. "
         ro.set_display_output("extended")
    if input in list_display_terms:
         result="You chose the normal display. "
         ro.set_display_output("standard_list")
    return result


def input_is_integer(input):
    """Determine if input is integer

    If it is an integer, return an integer.
    If not, lower case the input
       and see if it is something else.
    """
    result = ""
    try:
        term = int(input)
        result = input
    except ValueError:
        input = input.lower()
        result = check_if_modifier(input)
    return result


class index: 
    def GET(self): 
        form = myform()
        global ro 
        return render.formresult(form, ro)


    def POST(self): 
        form = myform() 
        global ro
        ro.zero_results_list() #  remove any previous results from previous searches
        ro.zero_modifier_flags() # remove any previous modifier flags.  Maybe we're no longer evil.
        myextras = ""
        if not form.validates(): 
            myresults = []
            return render.formresult(form, ro)
        else: 
            xml_element_results = []
            xml_id_results = []
            weed_out_duplicates = []
            text = ""
            searchterm = form.d.searchfield
            ### first, for debugging, capture original form input.
            ### comment out the next two lines for production use
            text = "You submitted: [%s]\n" % searchterm 
            ro.set_results_text(text)
            ### sanity check the data sent from the customer
            searchterm = handle_form_input.check_input_length(searchterm)
            searchterm = handle_form_input.scrub_form_input(searchterm)
            searchterm = searchterm.lower()  # lower case text for searching
            ### check if this is a True cry for help
            if handle_form_input.check_is_input_cry_for_help(searchterm):
                help_text = ro.get_results_text()
                help_text = help_text +  smfoo.display_help_text("html")    
                ro.set_results_text(help_text)
                return render.formresult(form, ro)
            smx = smxml.smxml()
            input_values = handle_form_input.split_input_keep_quotes(searchterm)
            #### look up synonyms before weeding out duplicates.
            #### put something in here to weed out duplicates
            #
            #### set standard list of keys for monster attributes
            makeys = ['alignment', 'name', 'prd', 'size']
            for input in input_values:
                result = input_is_integer(input)
                if type(result) == tuple: 
                    if result[0] == "yes":# we have a modifier, like +good
                        modifier_text = handle_modifier(str(result[1]))
                        myextras = ro.get_results_text() + modifier_text
                        ro.set_results_text(myextras)
                    else: # we have other text input, like "dog, riding" or "all"
                        ### check it for synonyms and normalize it
                        normalized_search_term = check_for_synonyms(str(result[1]))
                        try:
                            normalized_search_term = int(normalized_search_term)
                            xml_id_results = smx.search_for_id_attributes(normalized_search_term)
                        except ValueError:
                            xml_id_results = smx.search_for_monster_name(normalized_search_term)
                        #### if this list is empty, we have no monster names like 'dog"
                        #### assume it is a special quality search on a term like "blindsense'
                        if not xml_id_results:
                            xml_id_results = smx.search_for_monster_sq(normalized_search_term)
                else:  # we have an integer
                    xml_id_results = smx.search_for_id_attributes(result)
                mon_att_keys = ['name', 'prd', 'hit_dice', 'hit_points', 'special_qualities', 'size', 'alignment']
                for monster_id in xml_id_results:
                    monster_obj = smfoo.monster_object() # create new monster object
                    mon_dict ={}
                    mon_dict = smx.id_into_dict(monster_id, mon_att_keys)
                    for attribute in mon_att_keys:
                        try:
                            throwaway = getattr(monster_obj, "set_%s" % attribute)(mon_dict[attribute])
                        except KeyError:
                            throwaway = getattr(monster_obj, "set_%s" % attribute)("")
                        throwaway2 = monster_obj.set_name_w_link()
                    if monster_obj.get_name() not in weed_out_duplicates:
                        xml_element_results.append(monster_obj)
                        weed_out_duplicates.append(monster_obj.get_name())
                for r in xml_element_results:
                    if r not in ro.get_results_list():
                        ro.set_results_list(r)
            ### set HTML list or HTML table.  Default is list ###
            if ro.get_display_output() =="extended":
                ### hack to get Augmented Summoning to show up in extended display
                if "The Augment Summoning feat" in ro.get_results_text():
                    newlist=[]
                    for monster_obj in ro.get_results_list():
                        newlist.append(monster_obj)
                    ro.zero_results_list()
                    for mon_obj in newlist:
                        mon_obj.apply_augs_feat()
                        ro.set_results_list(mon_obj)
                return render.formresultextended(form, ro)
            else:
                return render.formresult(form, ro)



if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
