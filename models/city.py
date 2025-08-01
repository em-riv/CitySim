from models.buildings.building_type import BuildingType
from models.resources.resource_type import ResourceType
from models.buildings.house import House
from models.buildings.park import Park
from models.buildings.factory import Factory
from models.events.event import Event
from models.inhabitant import Inhabitant
from models.resources.water import Water
from models.resource.electricity import Electricity
from models.resource.food import Food


class City:
    """
        Class City which manage all the management of each event of the day
    """

    def __init__(self, name, arrivals: list = None):
        self.__name = name
        self.__list_building = []
        self.__stock = {
            "Water": 0,
            "Electricity": 0,
            "Food": 0
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
        message = f"City : {self.__name}\nResource: "
        for key, value in self.__stock.items():
            message += f"\t{key}: {value}\n"
        message += "Building:\n"
        for building in self.__list_building:
            message += f"\t{building.__str__()}\n"
        return message

    def add_building(self, building):
        if building.building_type == BuildingType.HOUSING:
            building = House("El bordel", 10)
        elif building.building_type == BuildingType.ENTERTAINMENT:
            building = Park("Boulogne park", float('inf'))
        elif building.building_type == BuildingType.PRODUCTION:
            if resources is None:
                raise ValueError("Factory is not working")
            resource = Electricity()
            building = Factory("AssCompact", 0, resource)

        else:
            raise ValueError("Invalide building type")
        self.__list_building.append(building)



    def produce_resources(self):
        list_factory = [building for building in self.__list_building if building.type is BuildingType.PRODUCTION]
        for building in list_factory:
            if building.resource_type is ResourceType.ELECTRICITY:
                self.__stock["Electricity"] += building.produce()
            elif building.resource_type is ResourceType.FOOD:
                self.__stock["Food"] += building.produce()
            elif building.resource_type is ResourceType.WATER:
                self.__stock["Water"] += building.produce()

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

    def assign_inhabitant(self):
        for inhabitant in self.arrivals:
            assigned = False

            # Trying houses first
            for building in self.__list_building:
                if isinstance(building, House) and building.assign_inhabitant(inhabitant):
                    inhabitant.has_roof = True
                    assigned = True
                    break

            # Trying parks next
            if not assigned:
                for building in self.__list_building:
                    if isinstance(building, Park) and building.assign_inhabitant(inhabitant):
                        inhabitant.has_roof = False
                        assigned = True
                        break

    def give_home(self):
        """Move inhabitants from parks to available houses"""

        # Find all park dwellers (people without proper homes)
        homeless = []
        for building in self.__list_building:
            if isinstance(building, Park):
                # Get copy of habitants list to avoid modification during iteration
                for inhabitant in building._Park__habitants[:]:  # Using name mangling to access private attribute
                    homeless.append((inhabitant, building))

        # Try to move them to houses
        for inhabitant, current_park in homeless:
            for building in self.__list_building:
                if isinstance(building, House) and building.assign_inhabitant(inhabitant):
                    # Successfully moved to house
                    inhabitant.has_roof = True
                    # Remove from park
                    current_park._Park__habitants.remove(inhabitant)
                    print(f"Moved {inhabitant} from park to house: {building._Building__name}")
                    break

if __name__ == "__main__" :
    city = City("Bruxelles")
    city.add_building(BuildingType.HOUSING)
    city.apply_event(Event.FIRE)
    city.apply_event(Event.NONE)
    city.apply_event(Event.FLOOD)
    city.apply_event(Event.STRIKE)
    city.apply_event(Event.LOCAL_CELEBRATION)
