class Inhabitant:

    """This class represents the inhabitant model of the city"""

    def __init__(self, name, age, profession, happiness=50, has_roof=False):
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__happiness = happiness
        self.__has_roof = has_roof

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.age

    @property
    def profession(self):
        return self.profession

    @property
    def happiness(self):
        return self.happiness

    @property.getter
    def happiness(self):
        return self.happiness

    @property
    def has_roof(self):
        return self.has_roof

    @property.getter
    def has_roof(self):
        return self.has_roof
