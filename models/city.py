
from models.buildings.building_type import BuildingType
from models.buildings.factory import Factory
from models.buildings.house import House
from models.buildings.park import Park
from models.events.event import Event
from models.inhabitant import Inhabitant
from models.resources.water import Water


class City:
    """
        Class City which manage all the management of each event of the day
    """
    def __init__(self, name, arrivals: list = None):
        self.__name = name
        self.__list_building = []
        self.__stock = {
            "Water": 0,
            "Electricity" : 0,
            "Food" : 0
        }
        self.arrivals = arrivals if arrivals is not None else []

    @property
    def population(self):
        # The population will be computed with all the House in list_building
        return 0

    @property
    def happiness(self):
        # The happiness will be dependent of all the inhabitant
        return 100

    def __str__(self):
        print(f"City : {self.__name}")
        print(f"Resource:")
        for key, value in self.__stock.items():
            print(f"\t{key}: {value}")
        print("Building")
        print(*self.__list_building)

    def add_building(self, building: BuildingType):
        citizen = Inhabitant("citizen 1", 12, "student")
        house = House("maison" , 5)
        house.assign_inhabitant(citizen)
        self.__list_building.append(house)

        park = Park("Central Park", 5)
        homeless = Inhabitant("homeless 1", 22, "unemployed")
        park.assign_inhabitant(homeless)
        self.__list_building.append(park)

        factory = Factory("Factory", 5 , Water())
        self.__list_building.append(factory)

    def produce_resources(self):
        pass

    def next_turn(self):
        pass

    def add_inhabitant(self, inhabitant):
        """
        Add an inhabitant to the city.
        """
        if not isinstance(inhabitant, Inhabitant):
            raise TypeError("Only Inhabitant objects can be added. Use Inhabitant class methods to create them.")
        self.arrivals.append(inhabitant)

    def add_random_inhabitants(self, count):
        """Add multiple random inhabitants to the city"""
        for _ in range(count):
            self.add_inhabitant(Inhabitant.create_random())

    def create_and_add_random(self):
        """Convenience method that creates and adds a random inhabitant"""
        new_inhabitant = Inhabitant.create_random()
        self.add_inhabitant(new_inhabitant)
        return new_inhabitant
    
    def apply_event(self, event: Event):
        for building in self.__list_building :
            building.building_damage(event.damages)
            if (isinstance(building, House) or isinstance(building, Park)) :
                inhabitants = building.inhabitants
                for inhabitant in inhabitants :
                    inhabitant.update_happiness(event.happiness)


if __name__ == "__main__" :
    city = City("Bruxelles")
    city.add_building(BuildingType.HOUSING)
    city.apply_event(Event.FIRE)
    city.apply_event(Event.NONE)
    city.apply_event(Event.FLOOD)
    city.apply_event(Event.STRIKE)
    city.apply_event(Event.LOCAL_CELEBRATION)
