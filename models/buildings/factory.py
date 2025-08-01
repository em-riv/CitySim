from models.buildings.building import Building
from models.buildings.building_type import BuildingType

from models.resources.electricity import Electricity
from models.resources.food import Food
from models.resources.water import Water
from models.resources.resource_type import ResourceType


class Factory(Building):

    def __init__(self, name, capacity, resources):
        super().__init__(name, capacity, BuildingType.PRODUCTION)
        self.__resources = resources

    @property
    def resource_type(self):
        if isinstance(self.__resources, Electricity):
            return ResourceType.ELECTRICITY
        elif isinstance(self.__resources, Food):
            return ResourceType.FOOD
        elif isinstance(self.__resources, Water):
            return ResourceType.WATER

    def produce(self):
        return self.__resources.collect()
