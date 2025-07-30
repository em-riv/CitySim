from models.resources.resource import Resource

import random

class Electricity(Resource):

    def __init__(self):
        # I give arbitrary number where must be changed once the functionnal analyse is done
        # TODO : Decide the correct value
        super().__init__(75)

    def collect(self):
        return random.randint(1,self.max_production)

if __name__ == "__main__":
    electric = Electricity()
    print(electric.collect())