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

    def get_current_sandwich(self):
        return self.__current_sandwich

    def load_available_ingredients(self):
        pass

    def load_availables_sizes(self):
        pass

    def generate_available_ingredients_dict(self):
        pass

    def generate_available_sizes_dict(self):
        pass

    def obtain_order_amount(self):
        return self.__order.calculate_order_price()
    
    def __search_available_sandwich_by_command(self, command : str) -> Sandwich:
        pass

    def prepare_sandwich(self: sandwich_command : str):
        pass
    
    def add_sandwich_to_order(self, sandwich_command : str):
        self.__order.add_sandwich(self.__search_available_sandwich_by_command(sandwich_command))
    
    def __search_available_ingredient_by_command(self, command : str) -> Sandwich:
        pass

    def add_ingredient_to_sandwich(self, ingredient_command : str):
        pass
    
    def make_sandwich(self, size : Size, ingredients : list):
        pass