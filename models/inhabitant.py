class Inhabitant:
    __name_list = []
    __professions = ["Engineer", "Teacher", "Doctor", "Artist", "Chef", "Lawyer", "Writer", "Nurse"]

    """This class represents the inhabitant model of the city"""

    def __init__(self, name, age, profession, happiness=50, has_roof=False):
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__happiness = happiness
        self.__has_roof = has_roof
        self.__load_names()

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

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
        return self.__has_roof

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

    @classmethod
    def __load_names(cls):
        """Load name from file once"""
        if cls.__name_list:
            cls.__name_list = []
            try:
                with open('prenom.txt', 'r', encoding = "utf-8") as f:
                    for line in f:
                        name = line.strip()
                        cls.__name_list.append(name)
            except FileNotFoundError:
                cls.__name_list = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
                print("Warning: prenom.txt not found, using default names")

    @classmethod
    def create_random(cls):
        """Create a random inhabitant with default values"""
        import random

        return cls(
            name =random.choice(cls.__name_list),
            age = random.randint(18, 65),
            profession = random.choice(cls.__professions),
            happiness = random.randint(30, 80),
            has_roof = False
        )
