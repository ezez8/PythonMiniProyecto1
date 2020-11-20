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
