from models.buildings.building_type import BuildingType
from inhabitant import Inhabitant

class City:
    """
        Class City which manage all the management of each event of the day
    """
    def __init__(self, name, arrivals=None):
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
        pass

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
