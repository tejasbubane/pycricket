#							pycricket
#		This is a small python script that takes in a name of a country and
#		pulls in the rss of the recent happenings in cricket related to that country
#		from espncricinfo, parses the xml file to get the appropriate strings
#		and displays the results.
#  Copyright (C) 2012  
#  Tejas Pramod Bubane (tejasbubane@gmail.com)
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

if sys.argv[1].lower() == 'india':	num = 6

if sys.argv[1].lower() == 'australia':	num = 2
	
if sys.argv[1].lower() == 'england':	num = 1

if sys.argv[1].lower() == 'south africa':	num = 3

if sys.argv[1].lower() == 'sri lanka':	num = 8

if sys.argv[1].lower() == 'west indies':	num = 4

if sys.argv[1].lower() == 'pakistan':	num = 7

if sys.argv[1].lower() == 'new zealand':	num = 5

os.system('wget --quiet http://www.espncricinfo.com/rss/content/feeds/news/'+str(num)+'.xml; mv '+str(num)+'.xml rss.xml')

fp = open('rss.xml','r')
data = fp.read()
s = 0
while 1:
	s = data.find('<title>',s+1)
	if s != -1:
		e = data.find('</title>',s+6)
		link = data[s+6:e]
		print link
	else:
		break
		
os.system('rm rss.xml')

#	Any suggestions/bugs/queries:
#  	Tejas Pramod Bubane (tejasbubane@gmail.com)
