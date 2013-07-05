summonmonsterfouroneone
=======================

 
Directory assistance for Summon Monster spells in the PFRPG


Description
===========

This application "summonmonsterfouroneone" is a tool to assist players with finding the right monster to summon using the various Summon Monster spells available in the PFRPG.

This application "summonmonsterfouroneone" or (sm411) 
will help players of the PFRPG with "Directory Assistance" 
searching  all possible monsters
that might be called
with various Summon Monster spells.


Why is this needed?  Suppose you are playing a character with access to the spell *Summon Monster V*.   This lets you summon one single monster from the fifth level monster list, between one and three monsters from the fourth level monster list, or between two and five monsters from any lower level list.   One of the options on the fourth level list is "mephit," which is actually a choice of one mephit out of the eight different types of mephit that may be summoned.  A different option is to summon an elemental, which is actually a choice out of four different elements.  One of those mephits can cast *Glitterdust* as a Spell Like Ability.  Can you remember which one?  I cannot.   That's one reason I built this tool.  Put *Glitterdust* in the search field, and it will come back with 'Mephit,Salt'. 


A second reason I built this tool has to do with Feats and Templates.   A spell caster with a Good alignment summons creatures with the  Celestial template.  A spell caster with an Evil alignment summons creatures with the  Infernal template.  A Neutral spell caster has another choice between Celestial and Infernal.  Can you remember all the abilities the template provides?  I cannot.   The "Augment Summoning" feat adds still more benefits to summoned creatures, notably a +4 CON bonus, so +2hp/HD.   This tool can apply that bonus.  If you search first for 'eagle' you will get base stats.  Search for 'eagle "+augment summoning"'  (or "eagle +a") and you will notice the Hit Points of the eagle have been modified by the Augment Summoning feat.


The reference to 4-1-1 is meant as a pun on Directory Assistance.



Description of use
------------------


Requirements
============


This application should require python 2.7 and nothing else.   Once I stop adding features, I intend to redo the application in python3.


I have access only to a UNIX (Ubuntu 12.04) host for development and testing.    If you are able to help improve this application for other operating systems, great, please do so.


Examples
========



Example of set up
-----------------

Source the file ./bin/setup.sh to set $PYTHONPATH environment variable.


    user@host: /path/to/summonmonsterfouroneone$ echo $PYTHONPATH
           
    user@host: /path/to/summonmonsterfouroneone$ . ./bin/setup.sh
    user@host: /path/to/summonmonsterfouroneone$ echo $PYTHONPATH
    :/path/to/summonmonsterfouroneone/sm411
    user@host: /path/to/summonmonsterfouroneone$ 
   


Example of use
--------------


Example of testing
------------------

summonmonsterfouroneone makes use of Unit Tests.  All tests are in the  tests/ directory.

Calling tests/rt.py with python runs a regression test framework of all files in tests/ that start with test_ and in with .py

    user@host: /path/to/summonmonsterfouroneone$ python tests/rt.py 
    ..................................................
    ----------------------------------------------------------------------
    Ran 50 tests in 0.027s
    
    OK
    user@host: /path/to/summonmonsterfouroneone$
    


Design Notes
============

1.  XML is case sensitive.  Searching XML is case sensitive.  The monster names are in lower case to avoid using two xpath functions at once.   So are most other elements with text that would be searched.  The translate() xpath function is not used to convert XML content to lower case.  Instead, this application uses only the contains() xpath function to search partial term input provided by the user.   All input terms are converted to lower case to make searching easier.
2.  The online PRD differs from the PFRPG book.  The online PRD has been corrected (or so it seems to me), so where there are differences from the book, I go with the online PRD.
3.  Not all the monsters available to the Summon Monster spells are in the xml data file at present.  

Licence
=======


The files in the OGL directory provide Open Gaming Content that is licenced under the Open Gaming Licence.  See the file OGL/licence.txt for more information. 

The file /static/js/jquery-latest.js is Copyright 2010, John Resig and distributed under the GNU General Public Licence.
The file /static/js/jquery.tablesorter.js is Copyright (c) 2007 Christian Bach and distributed under the GNU General Public Licence.


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



This application is not affiliated with Paizo.  


This application makes no claim to compatibility with the Pathfinder Role Playing Game made by Paizo.  




