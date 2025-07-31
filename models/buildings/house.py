from building import Building
from building_type import BuildingType

class House(Building):

    def __init__(self, name, capacity):
        super().__init__(name, capacity, BuildingType.HOUSING)
        self.__habitants = []

    def assign_inhabitant(self, inhabitant):
        if len(self.__habitants) < self.__capacity:
            self.__habitants.append(inhabitant)
            return True
        return False
