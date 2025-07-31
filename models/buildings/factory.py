from models.buildings.building import Building
from models.buildings.building_type import BuildingType

class Factory(Building):
 
    def __init__(self, name, capacity, resources ):
        super().__init__(name, capacity, BuildingType.PRODUCTION)
        self.__resources = resources
    
    def produce(self):
        return self.__resources.collect()
