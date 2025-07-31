from abc import ABC, abstractmethod 
from building_type import BuildingType

class Building(ABC):
    '''
    Absctract base class representing a building in a city simulation

    Attributs:
    - name (str): Name of building
    - capacity (int): Capacity of the building
    - integrity (int): Condition of the building (100% max, 0% min)
    - type (str): Type of the building

    Methodes:
    - building_damage(damage): deal damage
    - building_repair(repair): repair building
    - daily_building_passif(city): abstract methode for daily effect on the city
    - __str__(): return description of the building
    '''
    def __init__(self, name, capacity, integrity, type : BuildingType):
        '''
        Constructor
        Attributs:
        - name (str): Name of building
        - capacity (int): Capacity of the building
        - integrity (int): Condition of the building (100% max, 0% min)
        - type (str): Type of the building
        '''
        self.name = name
        self.capacity = capacity
        self.integrity = 100
        self.type = type

    def building_damage(self, damage):
        '''
        Deal demage
        Paramaters:
        - damages (int)

        '''
        self.integrity -=damage
        if self.integrity < 0:
            self.integrity = 0

    def building_repair(self, repair):
        '''
        Repair building
        Parameters:
        - repaire (int)
        '''
        self.integrity += repaire
        if self.integrity > 100:
            self.integrity = 100
    

    @abstractmethod
    def daily_building_passif(self, city):
        '''
        Abstracted methode
        Parameters:
        - city: Instance of the City class affected by the building
        '''
        pass

    def __str__(self):
        '''
        return description of the building
        '''
        return f"{self.name} ({self.type}) - state: {self.integrity}%, capacity: {self.capacity}"
