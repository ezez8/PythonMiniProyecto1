from Size import Size
from Ingredient import Ingredient

class Sandwich(object):
    def __init__(self):
        self.__size = None
        self.__ingredients = []

    def get_size(self):
        return self.__size
    
    def set_size(Self, size : Size):
        self.__size = Size

    def get_ingredients(self):
        return self.__ingredients

    def set_ingredients(self, ingredients : list):
        self.__ingredients =  ingredients
    
    def add_ingredient(self, ingredient : Ingredient):
        self.__ingredients.append(ingredient)
    
    def remove_ingredient(self, command : str):
        pass

    def calculate_price(self):
        price = self.__size if self.__size else 0
        for ingredient in self.__ingredients:
            price += ingredient.price
        return price
