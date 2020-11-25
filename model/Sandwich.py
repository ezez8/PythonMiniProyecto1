from model.Size import Size
from model.Ingredient import Ingredient

class Sandwich(object):
    """
    Clase utilizada para representar los sandwiches

    ...

    Attributes
    ----------
    size : Size
        Tamaño del sandwich
    ingredients_list : list
        Lista de ingrediente que contiene el sandwich

    Methods
    -------
    size(), size(value=Size)
        Getter y setter del atributo size
    ingredients_list(), ingredients_list(value=list)
        Getter y setter del atributo ingredients_list
    add_ingredient()
        Permite agregar un ingrediente a lista de ingredientes del sandwich
    remove_ingredient(command=str)
        Pemmite eleminar un ingrediente de la lista de ingredientes del sandwich
    modify_size(size=Size):
        Permite modificar el tamaño del sandwich
    calculate_price():
        Obtiene el costo total del sandwich
    get_small_description():
        Muestra la descripcion del sandwich indicando solo el tamaño
    get_full_description():
        Muestra la descripcion del sandwich indicando tamaño e ingredientes
    duplicate_sandwich(original):
        Metodo estatico que replica un sandwich
    
    """
    def __init__(self):
        self.size = None
        self.ingredients_list = []

    @property
    def size(self):
        """Getter del atributo size"""
        return self.__size
    
    def get_size(self):
        """retorna atributo size"""
        return self.size
    
    @size.setter
    def size(self, value : Size):
        """Setter del atributo size"""
        self.__size =  value
    
    @property
    def ingredients_list(self):
        """Getter del atributo ingredient_list"""
        return self.__ingredients_list
    
    def get_ingredient(self):
        """retorna el atributo ingredient_list"""
        return self.__ingredients_list
    
    @ingredients_list.setter
    def ingredients_list(self, value : list):
        """Setter del atributo ingredient_list"""
        self.__ingredients_list =  value
    
    def add_ingredient(self, ingredient : Ingredient):
        """Añade un ingrediente al sandwich"""
        self.ingredients_list.append(ingredient)
    
    def remove_ingredient(self, command : str):
        """elimina un ingrediente del sandwich"""
        self.ingredients_list.remove(command)

    def modify_size(self, size: Size):
        """Cambia la tamaño del sandwich"""
        self.size = size

    def calculate_price(self):
        """Retorna el costo total del sandwich"""
        price = self.size.price if self.size else 0
        for ingredient in self.ingredients_list:
            price += ingredient.price
        return price
    
    def get_small_description(self):
        """Muestra la descripcion del sandwich indicando solo el tamaño"""
        return self.size.name

    def get_full_description(self):
        """Muestra la descripcion del sandwich indicando tamaño e ingredientes"""
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
    
    @staticmethod
    def duplicate_sandwich(original):
        """Metodo estatico que replica un sandwich"""
        replica = Sandwich()
        replica.size = original.size
        for ingredient in original.ingredients_list:
            replica.add_ingredient(ingredient)
        return replica
