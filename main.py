import os

from core.logger.logger import Logger
from core.menu.menu_builder import MenuBuilder
from models.city import City

city = None
current_day = 0
def clear():
    input("Press enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def create_city():
    global city
    if city is None:
        name = input('Enter city name: ')
        city = City(name)
    else:
        print("City already exists. Do you want to reset it (y/n) ?")
        good_input = False
        while not good_input:
            choice = input(">").lower()
            if choice == 'y':
                good_input = True
                city = None
                create_city()
            elif choice == 'n':
                good_input = True
            else:
                print("Please enter y or n")
    print("Your city is created.")
    clear()


def add_building():
    print("Not implemented yet")
    clear()

def distribute_inhabitants():
    print("Not implemented yet")
    clear()

def pass_day():
    print("Not implemented yet")
    clear()

def show_log():
    global current_day
    logger = Logger()
    logs = logger.get_log_day(current_day)
    for l in logs:
        print(l)
    clear()

if __name__ == "__main__":

    menu = (MenuBuilder.add_option("Create City", create_city)
                        .add_option("Add Buildings", add_building)
                        .add_option("Distribute Inhabitants", distribute_inhabitants)
                        .add_option("Play a day", pass_day)
                        .add_option("Show log", show_log)
                        .add_option("Exit", exit)
                        .build())
    while True:
        menu.show()
