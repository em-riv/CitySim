from models.buildings.building_type import BuildingType
from models.resources.resource_type import ResourceType
from models.buildings.house import House
from models.buildings.park import Park
from models.buildings.factory import Factory
from models.events.event import Event
from models.inhabitant import Inhabitant
from models.resources.water import Water
from models.resources.electricity import Electricity
from models.resources.food import Food
from models.resources.resource_type import ResourceType


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
        self.__city_happiness = 0

    @property
    def population(self):
        # The population will be computed with all the House in list_building
        return 0

    @property
    def happiness(self):
        # The happiness will be dependent of all the inhabitant
        return self.__city_happiness

    def __str__(self):
        message = f"City : {self.__name}\nHappiness: {self.happiness}\nResource: "
        for key, value in self.__stock.items():
            message += f"\t{key}: {value}\n"
        message += "Building:\n"
        for building in self.__list_building:
            message += f"\t{building.__str__()}\n"
        return message

    def add_building(self, building, resource_type : ResourceType = None):
        if building.building_type == BuildingType.HOUSING:
            building = House("El bordel", 10)
        elif building.building_type == BuildingType.ENTERTAINMENT:
            building = Park("Boulogne park", float('inf'))
        elif building.building_type == BuildingType.PRODUCTION:
            if resource_type is None:
                raise ValueError("Factory is not working")
            resource = None
            match resource_type:
                case ResourceType.WATER:
                    resource = Water()
                case ResourceType.FOOD:
                    resource = Food()
                case ResourceType.ELECTRICITY:
                    resource = Electricity()
                case _:
                    raise ValueError("Unknown ResourceType")
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

    def next_turn(self, event: Event):
        self.__apply_event(event)

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

    def __apply_event(self, event: Event):
        for building in self.__list_building :
            building.building_damage(event.damages)
            if isinstance(building, House) or isinstance(building, Park):
                inhabitants = building.inhabitants
                for inhabitant in inhabitants :
                    inhabitant.update_happiness(event.happiness)

    def assign_inhabitant(self):
        for inhabitant in self.arrivals:
            assigned = False
            print(f"Assigning {inhabitant.name} a place to live")
            # Trying houses first
            for building in self.__list_building:
                if isinstance(building, House) and building.assign_inhabitant(inhabitant):
                    print(f"{inhabitant.name} find a home")
                    inhabitant.has_roof = True
                    assigned = True
                    break

            # Trying parks next
            if not assigned:
                for building in self.__list_building:
                    if isinstance(building, Park) and building.assign_inhabitant(inhabitant):
                        print(f"{inhabitant.name} find a nice place in the park")
                        inhabitant.has_roof = False
                        assigned = True
                        break
                if not assigned:
                    print(f"{inhabitant.name} remains a refugee")

    def give_home(self):
        """Move inhabitants from parks to available houses"""

        # Collect all homeless
        homeless = []
        for building in self.__list_building:
            if isinstance(building, Park):
                for inhabitant in building.inhabitants():
                    homeless.append((inhabitant, building))

        # Try to move each homeless to a house
        moved_count = 0
        for inhabitant, current_park in homeless:
            for building in self.__list_building:
                if isinstance(building, House):
                    if building.assign_inhabitant(inhabitant):
                        inhabitant.has_roof = True
                        current_park.remove_inhabitant(inhabitant)
                        moved_count += 1
                        print(f"Moved {inhabitant.name} from park to house")
                        break

        print(f"Successfully moved {moved_count} inhabitants from parks to houses")
        return moved_count

    def city_happiness(self):
        total_inhabitants = 0
        for building in self.__list_building:
            if not isinstance(building, Factory):
                total_inhabitants += len(building.inhabitants)
                for inhabitant in building.inhabitants():
                    self.__city_happiness += inhabitant.happiness

        total_inhabitants += len(self.arrivals)
        for homeless in self.arrivals:
            self.__city_happiness += homeless.happiness

        self.__city_happiness = self.__city_happiness // total_inhabitants

if __name__ == "__main__" :
    city = City("Bruxelles")
    city.add_building(BuildingType.HOUSING)
    city.apply_event(Event.FIRE)
    city.apply_event(Event.NONE)
    city.apply_event(Event.FLOOD)
    city.apply_event(Event.STRIKE)
    city.apply_event(Event.LOCAL_CELEBRATION)
