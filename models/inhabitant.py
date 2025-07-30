class Inhabitant:

    """This class represents the inhabitant model of the city"""

    def __init__(self, name, age, profession, happiness=50, has_roof=False):
        self.name = name
        self.age = age
        self.profession = profession
        self.happiness = happiness
        self.has_roof = has_roof