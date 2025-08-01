import os

from core.logger.logger import Logger
from core.menu.menu_builder import MenuBuilder
from models.city import City
from models.buildings.building_type import BuildingType
from models.resources.resource_type import ResourceType
from models.events.event import Event

city : City = None
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
    global city
    if city is None:
        print("you must creat a City firt !")
        clear()
        return

    print("Choose building type: \n[1] -House \n[2] -Park \n[3] -Factory")
    choice = int(input("Enter number: "))

    
    building_type = None
    recource_type = None

    if choice == 1:
        building_type = BuildingType.HOUSING
        city.add_building(building_type,recource_type)
        print(f"\n{building_type.name} successfully added to the City !\n")
    elif choice == 2:
        building_type = BuildingType.ENTERTAINMENT
        city.add_building(building_type,recource_type)
        print(f"\n{building_type.name} successfully added to the City !\n")
    elif choice == 3:
        building_type = BuildingType.PRODUCTION
        print("Choose your Factory type: \n[1] -Water production \n[2] -Food production \n[3] -Electricity production")
        choiceType = int(input("Enter number: "))
        match choiceType:
            case 1:
                recource_type = ResourceType.WATER
            case 2:
                recource_type = ResourceType.FOOD
            case 3:
                recource_type = ResourceType.ELECTRICITY
            case _:
                print("Invalide resource type !")
                clear()
                return
        city.add_building(building_type,recource_type)
        print(f"\n{building_type.name} successfully added to the City !\n")

    else:
        print("Invalide building type")
        clear()
           
 

def distribute_inhabitants():
    from math import ceil
    if city is None:
        print("There is not city created yet")
    else:
        nb_arrivals = ceil(10 * city.happiness/100)
        city.add_random_inhabitants(nb_arrivals)
        print(f"There are {nb_arrivals} refugees arriving in City.")
        city.assign_inhabitant()
    clear()

def pass_day():
    print("Sunrise")
    print("Generating a random event")
    event = Event.getRandomEvent()
    print(f"Event generated: {event.name}")
    city.next_turn(event)
    print("Sunset")
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
