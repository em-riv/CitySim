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
        return self.__profession

    @profession.setter
    def profession(self, value: str):
        self.__profession = value

    @property
    def happiness(self):
        return self.__happiness

    @property
    def has_roof(self):
        return self.has_roof

    @has_roof.setter
    def has_roof(self, value: bool):
        self.__has_roof = value

    def gain_happiness(self, value: int):
        if self.__happiness + value >= 100:
            self.__happiness = 100
        else:
            self.__happiness += value

    def lose_happiness(self, value: int):
        if self.__happiness - value <= 0:
            self.__happiness = 0
        else:
            self.__happiness -= value
