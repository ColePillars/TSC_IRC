import datetime
import sys
import urllib.request

from bs4 import BeautifulSoup


def query():  # Prints the top X results for a specific scoreboard
    # Input scoreboard information and number of items to display
    input_str = input('level.mission.type.howmany: ')
    input_arr = input_str.replace(' ', '').split('.')
    default_arr = ['city_escape','mission_1','times','1']
    actual_arr = ['','','','']

    # Inputs user information into corresponding spots in actual_arr
    for index, item in reversed(list(enumerate(input_arr[:], start=0))):
        actual_arr[index] = item

    # Inputs default information into corresponding empty spots in actual_arr
    for index in range(0, len(default_arr)):
        if actual_arr[index] == '':
            actual_arr[index] = default_arr[index]
    print("Query for: " + actual_arr[0] + " " + actual_arr[1] + " " + actual_arr[2])

    # Creates Output File
    with open(datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.output.txt', 'w') as f:
        # Creates the soup, with URL determined by Type/Level/Mission
        url = "http://www.soniccenter.org/rankings/sonic_adventure_2_b/" + actual_arr[2] + "/" + actual_arr[0] + "/" + \
              actual_arr[1]

        soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

        # Selects the table rows of interest
        innerdata = soup.find(class_="innerdata")
        rows = innerdata.find_all('tr')

        # Final row
        stopIndex = 1 + int(actual_arr[3])

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
                print(cell.get_text() + "\t", end="")

                # Adds tabs based on name length
                if cells.index(cell) == 1 and stopIndex > 2:
                    times = int(len(cell.get_text()) / 4)
                    while times < longestName:
                        print("\t", end="")
                        f.write("\t")
                        times += 1
            print(str(title))
            f.write(str(title))
            f.write("\n")


def list_options():  # Lists the scoreboards available
    # #times #rings #scores #races #bosses #freestyle
    # Input type to be listed
    input_str = input('Enter Type Here: ')

    # Creates Output File
    with open(datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.output.txt', 'w') as f:

        # Creates the soup, with URL determined by Type
        url = "http://www.soniccenter.org/rankings/sonic_adventure_2_b/" + input_str
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

        # Selects the table rows of interest
        innerdata = soup.find(class_="innerdata")
        rows = innerdata.find_all('tr')

        # Loop of table rows
        for row in rows[1:]:
            cells = row.find_all('td')

            # Only prints cells with information
            if cells[0].get_text() != "":
                f.write(cells[0].get_text() + "\n")


def main():  # Option Select
    while True:
        try:
            what_do = int(input('Exit:\t0 \nQuery:\t1 \nList:\t2 \n'))
            if what_do == 0:
                break
            if what_do == 1:
                query()
            if what_do == 2:
                list_options()
        except:
            continue


if __name__ == "__main__":
    main()
else:
    sys.exit()