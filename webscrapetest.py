import datetime
import urllib.request

from bs4 import BeautifulSoup


# Prints the top X results for a specific scoreboard
def query():
    # Input scoreboard information and number of items to display
    inputStr = input('type.level.mission.howmany: ')
    inputArr = inputStr.split('.')

    # Creates the soup, with URL determined by Type/Level/Mission
    URL = "http://www.soniccenter.org/rankings/sonic_adventure_2_b/" + inputArr[0] + "/" + inputArr[1] + "/" + inputArr[
        2]
    soup = BeautifulSoup(urllib.request.urlopen(URL).read(), "html.parser")

    # Selects the table rows of interest
    innerdata = soup.find(class_="innerdata")
    rows = innerdata.find_all('tr')

    # Final row
    stopIndex = 1 + int(inputArr[3])

    # Loop of table rows up to the number specified
    for row in rows[1:stopIndex]:
        cells = row.find_all('td')
        try:
            title = cells[2]['title']
        except:
            title = ""

        # Loop through data in each table row
        for cell in cells[1:]:
            f.write(cell.get_text() + "\t")

            # Adds tabs based on name length
            if cells.index(cell) == 1 and stopIndex > 2:
                times = int(len(cell.get_text()) / 8)
                while times < 2:
                    f.write("\t")
                    times = times + 1
        f.write(str(title))
        f.write("\n")

    # Makes the information instantly print to file instead of waiting
    f.flush()


# Lists the scoreboards available
def listOptions():
    # times #rings #scores #races #bosses #freestyle
    # Input type to be listed
    inputStr = input('Enter Type Here: ')

    # Creates the soup, with URL determined by Type
    URL = "http://www.soniccenter.org/rankings/sonic_adventure_2_b/" + inputStr
    soup = BeautifulSoup(urllib.request.urlopen(URL).read(), "html.parser")

    # Selects the table rows of interest
    innerdata = soup.find(class_="innerdata")
    rows = innerdata.find_all('tr')

    # Loop of table rows
    for row in rows[1:]:
        cells = row.find_all('td')

        # Only prints cells with information
        if cells[0].get_text() != "":
            f.write(cells[0].get_text() + "\n")
    f.flush()


# Option Select
while (True):
    try:
        whatdo = int(input('Exit:\t0 \nQuery:\t1 \nList:\t2 \n'))
        if whatdo == 0:
            exit()
        if whatdo == 1:
            f = open(datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.txt', 'w')
            query()
        if whatdo == 2:
            f = open(datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.txt', 'w')
            listOptions()
    except:
        continue
