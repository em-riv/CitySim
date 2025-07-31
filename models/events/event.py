from enum import Enum
from random import choice

from models.events.event_impact import EventImpact

class Event(Enum):
    """ Enum that represents all the events that can happen in a city, with their impact on buildings and people """

    NONE = EventImpact()
    FIRE = EventImpact(damages=10)
    FLOOD = EventImpact(damages=10)
    STRIKE = EventImpact(happiness=-5)
    LOCAL_CELEBRATION = EventImpact(happiness=10)

    @property
    def happiness(self):
        return self.value.happiness
    
    @property
    def damages(self):
        return self.value.damages

    @classmethod
    def getRandomEvent(cls):
        """ returns a random Event """
        events = list(cls)
        return choice(events)
                                 
                            
if __name__ == "__main__":
    print(f"Fire happiness: {Event.FIRE.happiness}")
    print(f"Fire damages: {Event.FIRE.damages}")
    print(f"Random Event: {Event.getRandomEvent()}")
