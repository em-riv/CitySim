from abc import ABC, abstractmethod

class Resource(ABC):
    """
        Abstract class which determine the behaviour of the resources
    """

    def __init__(self, max_production):
        self.max_production = max_production

    @abstractmethod
    def collect(self) -> int:
        """
            Method which will give the number of resource can be collected by day
        """
        pass