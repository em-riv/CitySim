from models.buildings.building_type import BuildingType


class City:
    """
        Class City which manage all the management of each event of the day
    """
    def __init__(self, name):
        self.__name = name
        self.__list_building = []
        self.__stock = {
            "Water": 0,
            "Electricity" : 0,
            "Food" : 0
        }

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

