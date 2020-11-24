from model.Order import Order
from model.Sandwich import Sandwich
from model.Size import Size
from model.Ingredient import Ingredient
from model.Size import Size
from pathlib import Path
class Model(object):
    
    def __init__(self):
        self.__available_ingredients = []
        self.__available_sizes = []
        self.__order = Order()
        self.__current_sandwich = None
        self.__current_ingredient = None

    def get_order(self):
        return self.__order
    
    def get_available_ingredients(self):
        return self.__available_ingredients
    
    def get_available_sizes(self):
        return self.__available_sizes

    def get_current_sandwich(self):
        return self.__current_sandwich

    def get_order(self):
        return self.__order

    def load_available_ingredients(self):
        base_path = Path(__file__).parent
        file_path = (base_path / "../config/ingredients.txt").resolve()
        ingredients_list = self.__read_file_lines(file_path)
        for name,command,price in ingredients_list:
            self.__available_ingredients.append(Ingredient(name,command,price))
        
    def load_availables_sizes(self):
        base_path = Path(__file__).parent
        file_path = (base_path / "../config/sizes.txt").resolve()
        sizes_list = self.__read_file_lines(file_path)
        for name,command,price in sizes_list:
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

    def generate_available_ingredients_dict(self) -> dict:
        ingredients_dict = {}
        for ingredient in self.__available_ingredients :
            ingredients_dict[ingredient.command] = ingredient.name
        return ingredients_dict

    def generate_available_sizes_dict(self) -> dict:
        sizes_dict = {}
        for size in self.__available_sizes :
            sizes_dict[size.command] = size.name
        return sizes_dict

    def obtain_order_amount(self):
        return self.__order.calculate_order_price()

    def set_sandwich_size(self, size_command : str):
        self.__current_sandwich.size = self.__search_available_size_by_command(size_command)

    def prepare_sandwich(self, size_command : str):
        self.__current_sandwich = Sandwich()
        self.set_sandwich_size(size_command)
    
    def add_sandwich_to_order(self):
        self.__order.add_sandwich(self.__current_sandwich)

    def add_cloned_sandwich_to_order(self, sandwich_index: int, number_copy: int):
        sandwich_to_copy = self.__order.get_sandwiches()[sandwich_index]
        for _ in range(number_copy):
            self.__order.add_sandwich(Sandwich.duplicate_sandwich(sandwich_to_copy))
    
    def __search_available_ingredient_by_command(self, command : str) -> Sandwich:
        ingredient = None
        for item in self.__available_ingredients:
            if item.command == command:
                ingredient = item
                break
        return ingredient

    def __search_available_size_by_command(self, command : str) -> Size:
        size = None
        for item in self.__available_sizes:
            if item.command == command:
                size = item
                break
        return size

    def add_ingredient_to_sandwich(self, ingredient_command : str):
        self.__current_sandwich.add_ingredient(self.__search_available_ingredient_by_command(ingredient_command))

    def add_ingredient_to_specific_sandwich(self, ingredient_command:str, sandwich: Sandwich):
        sandwich.add_ingredient(self.__search_available_ingredient_by_command(ingredient_command))

    def modify_size_to_specific_sandwich(self, size_command:str, sandwich: Sandwich):
        sandwich.modify_size(self.__search_available_size_by_command(size_command))
    
    def delete_ingredient_to_specific_sandwich(self, ingredient_command:str, sandwich: Sandwich):
        sandwich.remove_ingredient(self.__search_available_ingredient_by_command(ingredient_command))

    def obtain_total_price(self):
        return self.__order.calculate_order_price()

    def generate_sandwich_options_dict(self):
        options_dict = { 'q' : 'Salir'}
        for index,sandwich in enumerate(self.__order.get_sandwiches()):
            options_dict[str(index + 1)] = sandwich.get_full_description()
        return options_dict
    
    def get_number_sandwich_order(self):
        return self.__order.get_number_of_sandwiches()
    
    def reset_order(self):
        self.__order = Order()
        self.__current_sandwich = None
        self.__current_ingredient = None
