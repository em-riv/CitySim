from building_type import BuildingType

class Building:
    '''
    Methodes:
    - building_damage(damage): deal damage
    - building_repair(repair): repair building
    - __str__(): return description of the building
    '''
    def __init__(self, name, capacity, type : BuildingType):
        '''
        Constructor
        Attributs:
        - __name (str): Name of building
        - __capacity (int): Capacity of the building
        - __integrity (int): Condition of the building (100% max, 0% min)
        - __type (str): Type of the building
        '''
        self.__name = name
        self.__capacity = capacity
        self.__integrity = 100
        self.__type = type

    def building_damage(self, damage):
        '''
        Deal demage
        Paramaters:
        - damages (int)

        '''
        self.__integrity -= damage
        if self.__integrity < 0:
            self.__integrity = 0

    def building_repair(self, repair):
        '''
        Repair building
        Parameters:
        - repair (int)
        '''
        self.__integrity += repair
        if self.__integrity > 100:
            self.__integrity = 100
    

    def __str__(self):
        '''
        return description of the building
        '''
        return f"{self.__name} ({self.__type}) - state: {self.__integrity}%, capacity: {self.__capacity}"
