from model.Size import Size
from model.Ingredient import Ingredient

class Sandwich(object):
    def __init__(self):
        self.size = None
        self.ingredients_list = []

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value : Size):
        self.__size =  value
    
    @property
    def ingredients_list(self):
        return self.__ingredients_list
    
    @ingredients_list.setter
    def ingredients_list(self, value : list):
        self.__ingredients_list =  value
    
    def add_ingredient(self, ingredient : Ingredient):
        self.ingredients_list.append(ingredient)
    
    def remove_ingredient(self, command : str):
        pass

    def calculate_price(self):
        price = self.size.price if self.size else 0
        for ingredient in self.ingredients_list:
            price += ingredient.price
        return price
    
    def get_small_description(self):
        return self.size.name

    def get_full_description(self):
        size_section = self.size.name

        ingredients_list = [ingredient.name for ingredient in self.ingredients_list]
        number_of_ingredients = len(ingredients_list)
        ingredients_section = ''
        if  number_of_ingredients == 0:
            ingredients_section = ''
        elif number_of_ingredients == 1:
            ingredients_section = f' con {ingredients_list[0]}'
        else:
            first_part = ', '.join(ingredients_list[0:-1])
            last_part = ingredients_list[-1]
            ingredients_section = f' con {first_part} y {last_part}'
        
        return f'{size_section}{ingredients_section}'
