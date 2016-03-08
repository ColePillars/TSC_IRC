import datetime
import sys
import urllib.request

from bs4 import BeautifulSoup


def query():  # Prints the top X results for a specific scoreboard
    # Input scoreboard information and number of items to display
    input_arr = input('level.mission.type.howmany: ').replace(' ', '').split('.')
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
        stop_index = max(2, 1 + int(actual_arr[3]))

        # Finds Longest Name
        longest_name = 0
        longest_record = 0
        for row in rows[1:stop_index]:
            cells = row.find_all('td')
            longest_name = max(longest_name, int(len(cells[1].get_text()) / 4))
            longest_record = max(longest_record, int(len(cells[2].get_text()) / 4))

        # Prints first person to obtain record if query is for 1 record
        if stop_index == 2:
            record = []
            bool_val = True
            while bool_val:
                for row in rows[1:]:
                    cells = row.find_all('td')
                    if not record:
                        record = cells
                    elif int(cells[0].get_text()) == 1:
                        # If statement determines which date is older
                        if int(cells[3].get_text()[6:]) < int(record[3].get_text()[6:]) or \
                                (int(cells[3].get_text()[:2]) < int(record[3].get_text()[:2]) and
                                         int(cells[3].get_text()[6:]) == int(record[3].get_text()[6:])) or \
                                (int(cells[3].get_text()[3:5]) < int(record[3].get_text()[3:5]) and
                                         int(cells[3].get_text()[:2]) == int(record[3].get_text()[:2]) and
                                         int(cells[3].get_text()[6:]) == int(record[3].get_text()[6:])):
                            record = cells
                    else:
                        bool_val = False
            print("Runner: " + record[1].get_text() + "\t Record: " + record[2].get_text() + "\t Date: " +
                  record[3].get_text() + "\t Comment: ", end="")
            f.write("Runner: " + record[1].get_text() + "\t Record: " + record[2].get_text() + "\t Date: " +
                    record[3].get_text()+ "\t Comment: ")
            try:
                print(record[2]['title'])
                f.write(record[2]['title'] + "\n")
            except:
                print()
                f.write("\n")

        # Prints records up to the number specified
        if stop_index > 2:
            for row in rows[1:stop_index]:
                cells = row.find_all('td')

                # Prints runners name and tabs determined by length of runners name
                print("Runner: " + cells[1].get_text() + "\t", end="")
                f.write("Runner: " + cells[1].get_text() + "\t")
                times = int(len(cells[1].get_text()) / 4)
                while times < longest_name:
                    print("\t", end="")
                    f.write("\t")
                    times += 1

                # Prints record and tabs determined by length of record
                print("Record: " + cells[2].get_text() + "\t", end="")
                f.write("Record: " + cells[2].get_text() + "\t")
                times = int(len(cells[2].get_text()) / 4)
                while times < longest_record:
                    print("\t", end="")
                    f.write("\t")
                    times += 1

                # Prints Date and Comment of record
                print("Date: " + cells[3].get_text() + "\tComment: ", end="")
                f.write("Date: " + cells[3].get_text() + "\tComment: ")
                try:
                    print(cells[2]['title'])
                    f.write(cells[2]['title'] + "\n")
                except:
                    print()
                    f.write("\n")


def list_options():  # Lists the scoreboards available
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

            # Supposed to print mission #'s
            try:
                print(cells[0].get_text().replace(' ', '_').replace('\'', '') + "\t" + cells[1]['title'])
                f.write(cells[0].get_text().replace(' ', '_').replace('\'', '') + "\t" + cells[1]['title'] + "\n")
            except:
                print(cells[0].get_text().replace(' ', '_').replace('\'', '') + "\t")
                f.write(cells[0].get_text().replace(' ', '_').replace('\'', '') + "\t" + "\n")


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