import urllib.request
import datetime
from bs4 import BeautifulSoup

#Prints the top X results for a specific scoreboard
def query():
	#Input scoreboard information and number of items to display
	Type = input('Enter Type Here: ')
	Level = input('Enter Level Here: ')
	Mission = input('Enter Mission Here: ')
	Howmany = input('Enter How Many Here: ')
	
	#Creates the soup, with URL determined by Type/Level/Mission
	URL = "http://www.soniccenter.org/rankings/sonic_adventure_2_b/" + Type + "/" + Level + "/" + Mission
	soup = BeautifulSoup(urllib.request.urlopen(URL).read(), "html.parser")
	
	#Selects the table rows of interest
	innerdata = soup.find(class_="innerdata")
	rows = innerdata.find_all('tr')

	#Final row 
	Stopindex = 1 + int(Howmany)
	
	#Loop of table rows up to the number specified
	for row in rows[1:Stopindex]:
		cells = row.find_all('td')
		
		#Loop through data in each table row
		for cell in cells[1:]:
			f.write(cell.get_text() + "\t")
			
			#Adds tabs based on name length
			if cells.index(cell) == 1 and Stopindex > 2:
				times = int(len(cell.get_text())/8)
				while times < 2:
					f.write("\t")
					times = times + 1
		f.write("\n")
	f.flush()

#Lists the scoreboards available
def list():
	#times #rings #scores #races #bosses #freestyle
	
	#Input type to be listed
	Type = input('Enter Type Here: ')
	
	#Creates the soup, with URL determined by Type
	URL = "http://www.soniccenter.org/rankings/sonic_adventure_2_b/" + Type
	soup = BeautifulSoup(urllib.request.urlopen(URL).read(), "html.parser")
	
	#Selects the table rows of interest
	innerdata = soup.find(class_="innerdata")
	rows = innerdata.find_all('tr')
	
	#Loop of table rows
	for row in rows[1:]:
		cells = row.find_all('td')
		
		#only prints cells with information
		if cells[0].get_text() != "":
			f.write(cells[0].get_text() + "\n")
	f.flush()



#
while(True):
	#Creates file with current date and time in the name
	whatdo = int(input('Exit:\t0 \nQuery:\t1 \nList:\t2 \n'))
	if whatdo == 0:
		break
	if whatdo == 1:
		f = open(datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.txt', 'w')
		query()
	if whatdo == 2:
		f = open(datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.txt', 'w')
		list()


#PROBABLY NOT IMPORTANT

#f = open(datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.txt', 'w')
#f.write(str(rows))

#http://colepillars.com
#http://www.soniccenter.org/rankings/sonic_adventure_2_b
#print soup.prettify()
#print(soup.get_text())

#import urllib2
#from bs4 import BeautifulSoup

#f = open(variable + '.html', 'w')
#for link in soup.find_all("a", class_="innerdata"):
#    print(link.get('href'))

#variable = input('Enter Something Here: ')