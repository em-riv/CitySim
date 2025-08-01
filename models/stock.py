class Stock:

    def __init__(self, water = 10, electricity = 10, food = 10):
        self.__water = water
        self.__electricity = electricity
        self.__food = food

    def consume_water(self):
        if self.__water > 0 : 
            self.__water -= 1
            return True
        else : return False
        
    def consume_electricity(self):
        if self.__electricity > 0 : 
            self.__electricity -= 1
            return True
        else : return False

    def consume_food(self):
        if self.__food > 0 : 
            self.__food -= 1
            return True
        else : return False

    def stock_water(self, quantity):
        self.__water += quantity

    def stock_electricity(self, quantity):
        self.__electricity += quantity

    def stock_food(self, quantity):
        self.__food += quantity
        