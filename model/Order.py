from model.Sandwich import Sandwich

class Order(object):

    def __init__(self):
        self.__sandwiches = []
    
    def get_sandwiches(self):
        return self.__sandwiches
    
    def set_sandwiches(self, sandwiches : list):
        self.__sandwiches = sandwiches
    
    def add_sandwich(self, sandwich : Sandwich):
        self.__sandwiches.append(sandwich)
    
    def remove_sandwich(self, id : int):
        del self.__sandwiches[id-1]

    def calculate_order_price(self):
        price = 0
        for sandwich in self.__sandwiches:
            price += sandwich.calculate_price()
        return price
    
    def get_number_of_sandwiches(self):
        return len(self.__sandwiches)