from model.Order import Order
from model.Sandwich import Sandwich
from model.Size import Size
from model.Ingredient import Ingredient
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
        filepath = './../config/ingredients.txt'
        ingredients_list = self.__read_file_lines(filepath)
        for name,command,price in ingredients_list:
            self.__available_ingredients.append(Ingredient(name,command,price))

    def load_availables_sizes(self):
        filepath = './../config/sizes.txt'
        sizes_list = self.__read_file_lines(filepath)
        for name,command,price in ingredient_list:
            self.__available_sizes.append(Size(name,command,price))

    def __read_file_lines(self, filepath : str):
        tuple_lines = []
        try:
            with open(filepath) as f:
                lines = f.readlines()
            for line in lines:
                line_parts = line.strip('\n').strip('\r').split(' ')
                try:
                    price = float(line_parts[-1])
                    command = line_parts[-2]
                    name = ' '.join(line_parts[0:-2])
                    tuple_lines.append((name,command,price))
                except :
                    pass
        except FileNotFoundError as e:
            pass
        finally:
            return tuple_lines

    def generate_available_ingredients_dict(self):
        pass

    def generate_available_sizes_dict(self):
        pass

    def obtain_order_amount(self):
        return self.__order.calculate_order_price()
    
    def __search_available_sandwich_by_command(self, command : str) -> Sandwich:
        pass

    def prepare_sandwich(self, sandwich_command : str):
        pass
    
    def add_sandwich_to_order(self, sandwich_command : str):
        self.__order.add_sandwich(self.__search_available_sandwich_by_command(sandwich_command))
    
    def __search_available_ingredient_by_command(self, command : str) -> Sandwich:
        pass

    def add_ingredient_to_sandwich(self, ingredient_command : str):
        pass
    
    def make_sandwich(self, size : Size, ingredients : list):
        pass
