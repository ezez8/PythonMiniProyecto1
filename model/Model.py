from model.Order import Order
from model.Sandwich import Sandwich
from model.Size import Size
class Model(object):
    
    def __init__(self):
        self.__available_ingredients = []
        self.__available_sizes = []
        self.__order = Order()
        self.__current_sandwich = None
        self.__current_ingredient = None
    
    def get_available_ingredients(self):
        return self.__available_ingredients
    
    def get_available_sizes(self):
        return self.__available_sizes

    def load_available_ingredients(self):
        pass

    def load_availables_sizes(self):
        pass

    def obtain_order_amount(self):
        return self.__order.calculate_order_price()
    
    def add_sandwich_to_order(self, sandwich : Sandwich):
        self.__order.add_sandwich(sandwich)
    
    def make_sandwich(self, size : Size, ingredients : list):
        pass