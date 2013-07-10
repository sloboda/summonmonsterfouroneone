#!/usr/bin/env python 
""" smxml   Summon Monster XML

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





This is not "Summon a Monster Size (big) xml file"  :-) 

This file has the XML subroutines for unit testing
used by webserver.py and other applications
when filtering monster.xml 
to return only a subset of information.

"""

#####################################################################
#  for xml searching
#
from lxml import etree


class smxml:
    def setup_xml(self):
        ### specify path to xml file
        xmlfile = "./OGL/monsters.xml"
        t = etree.parse(xmlfile)
        return t


    def search_for_monster_sq(self, monster_sq_term="blindsense"):  
        """search xml for a monster special quality term

        The contains(text, searchterm) method in the lxml call 
              allows for input like "blindse" to match "blindsense"

        Returns a list of id values.  
        Each id value provides a single match 
          on an attribute "id" in a monster element in the XML file.
        """
        result = []
        smxl = smxml()
        t = smxl.setup_xml()
        monster_sq_term = monster_sq_term.lower()
        mypathval="""./monster/special_qualities/sq[contains(text(), '""" + str(monster_sq_term) +"""') ]/../.."""
        for m in t.xpath(mypathval):
             mid = m.get("id")
             result.append(mid)
        return result


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


    def monster_takes_c_or_i_template(self, mylistofID=['100']):
        """checks to see if monster element in XML file 
            has a "takes_c_or_i_template" element

        Expects list of monster id e.g.  ['100', '101']
        
        returns True or False
        """
        result=False  # assume it does not, to start
        elements = ["takes_c_or_i_template"]
        smxl = smxml()
        t = smxl.setup_xml()
        for mid in mylistofID:
            mysubpath= "./monster[@id='" + str(mid) + "']"
            for mvalue in t.xpath(mysubpath):
                children_list = mvalue.getchildren()
                for child in children_list:
                    if child.tag == elements[0]:
                        result = True
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
                        # test that parent element has a "special_qualities" element
                        if mvalue.find(k) is not None: 
                            for subele in mvalue.find(k).getchildren():
                                mylist.append(subele.text)
                            result[k] = mylist
                        else:
                            pass
                    else:
                        if mvalue.find(k) is not None:
                            result[k] = mvalue.find(k).text
                        else:
                            pass # we've been passed a key that does not exist
        return result







