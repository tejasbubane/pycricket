#						:::	  pycricket	 :::
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

import urllib2
from xml.dom import minidom

print('''
		-1. Live Scores
		0. World News

	News specific to a country:	
		1. England
		2. Australia
		3. South Africa
		4. west Indies
		5. New Zealand
		6. India
		7. Pakistan
		8. Sri Lanka

>>> Enter your choice: ''')

num = input()

if num == -1:
	rss = urllib2.urlopen('http://www.espncricinfo.com/rss/livescores.xml').read()
else:
	rss = urllib2.urlopen('http://www.espncricinfo.com/rss/content/feeds/news/'+str(num)+'.xml').read()

rssp = minidom.parseString(rss)

titles = rssp.getElementsByTagName('title')
links = rssp.getElementsByTagName('link')

for i in xrange(1, len(titles)):  # start from 1 to skip first title of espncricinfo
	title = titles[i].childNodes[0].nodeValue
	link = links[i].childNodes[0].nodeValue
	print('\n%d. %s :: %s' %(i, title, link))



#	Any suggestions/bugs/queries:
#  	Tejas Pramod Bubane (tejasbubane@gmail.com)
