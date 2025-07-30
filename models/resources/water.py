from models.resources.resource import Resource

import random

class Water(Resource):

    def __init__(self):
        # I give arbitrary number where must be changed once the functionnal analyse is done
        # TODO : Decide the correct value
        super().__init__(100)

    def collect(self):
        return random.randint(1, self.max_production)

if __name__ == "__main__":
    water = Water()
    print(water.collect())