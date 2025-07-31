from models.buildings.building import Building
from models.buildings.building_type import BuildingType

class Park(Building):
    
    def __init__(self, name, capacity):
        super().__init__(name, capacity, BuildingType.ENTERTAINMENT)
        self.__inhabitants = []

    @property
    def inhabitants(self):
        return self.__inhabitants

    def assign_inhabitant(self, inhabitant):        
        if len(self.__inhabitants) < self._capacity:
            self.__inhabitants.append(inhabitant)
            return True
        return False

    def bring_happiness(self):
        return 15