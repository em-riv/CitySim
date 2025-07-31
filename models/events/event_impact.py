class EventImpact:
    """ Class that represents the impact of an Event in term of happiness and damages to buildings """

    def __init__(self, happiness = 0, damages = 0):
        self.__happiness = happiness
        self.__damages = damages

    @property
    def happiness(self):
        return self.__happiness
    
    @property
    def damages(self):
        return self.__damages
