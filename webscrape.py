import datetime
import sys
import urllib.request

from bs4 import BeautifulSoup


def query():  # Prints the top X results for a specific scoreboard
    # Input scoreboard information and number of items to display
    inputStr = input('type.level.mission.howmany: ')
    inputArr = inputStr.split('.')

    # Creates Output File
    f = open(datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.output.txt', 'w')

    # Creates the soup, with URL determined by Type/Level/Mission
    URL = "http://www.soniccenter.org/rankings/sonic_adventure_2_b/" + inputArr[0] + "/" + inputArr[1] + "/" + inputArr[
        2]
    soup = BeautifulSoup(urllib.request.urlopen(URL).read(), "html.parser")

    # Selects the table rows of interest
    innerdata = soup.find(class_="innerdata")
    rows = innerdata.find_all('tr')

    # Final row
    stopIndex = 1 + int(inputArr[3])

    # Finds Longest Name
    longestName = 0
    for row in rows[1:stopIndex]:
        cells = row.find_all('td')
        for cell in cells[1:2]:
            longestName = max(longestName, int(len(cell.get_text()) / 4))

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
                times = int(len(cell.get_text()) / 4)
                while times < longestName:
                    f.write("\t")
                    times += 1
        f.write(str(title))
        f.write("\n")

    # Closes Output File
    f.close()


def list_options():  # Lists the scoreboards available
    # #times #rings #scores #races #bosses #freestyle
    # Input type to be listed
    inputStr = input('Enter Type Here: ')

    # Creates Output File
    f = open(datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.output.txt', 'w')

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

    # Closes Output File
    f.close()


# Option Select
def main():
    while True:
        try:
            whatdo = int(input('Exit:\t0 \nQuery:\t1 \nList:\t2 \n'))
            if whatdo == 0:
                break
            if whatdo == 1:
                query()
            if whatdo == 2:
                list_options()
        except:
            continue


if __name__ == "__main__":
    main()
else:
    sys.exit()
