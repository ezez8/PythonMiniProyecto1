from model.Order import Order
from model.Sandwich import Sandwich
from model.Size import Size
from model.Ingredient import Ingredient
from model.Size import Size
from pathlib import Path
class Model(object):
    """
    Clase utilizada para representar el modeo del patron MVC

    ...

    Attributes
    ----------
    available_ingredients : list
        Listado de ingrediente que maneja el sistema
    available_sizes : list
        Listado de tamaños de sandwiches que maneja el sistema
    order: Order
        Orden creada por los usuarios
    current_sandwich : Sandwich
        Atributo auxiliar para creación de sandwiches
    current_ingredient
        Atributo auxiliar para eliminación de ingrecientes

    Methods
    -------
    get_order():
        Getter del atributo order
    get_available_ingredients():
        Getter del atributo available_ingredients
    get_available_sizes():
        Getter del atributo available_sizes
    get_current_sandwich():
        Getter del atributo current_sandwich
    load_available_ingredients():
        Carga los ingregientes al sistema, leyendo el archivo ingrediens.txt
    load_availables_sizes():
        Carga los tamaños de panes en el sistema, leyendo el atchivp sizes.txt
    generate_available_ingredients_dict() -> dict:
        Retorna el diccionario donde las llaves son comando y los valores
        son los ingrediente que maneja el sistema
    generate_available_sizes_dict() -> dict:
        Retorna el diccionario donde las llaves son comando y los valores
        son los tamaños de sandwiches que maneja el sistema
    obtain_order_amount():
        Calcula el costo total de la orden
    set_sandwich_size(size_comman = str):
        Asigna un tamaño al sadwich referenciado por el atributo current_sandwich
    prepare_sandwich(size_command = str):
        Inicia el proceso de creación de sandwiches
    add_sandwich_to_order():
        Agrega un sandwich a la orden
    add_cloned_sandwich_to_order(sandwich_index= int, number_copy= int):
        Clona un sandwich de la orden tantas veces como indique el parametro number_copy
    add_ingredient_to_sandwich(ingredient_command = str):
        Agrega un ingrediente al sandwich referenciado por el atributo current_sandwich
    add_ingredient_to_specific_sandwich(ingredient_command=str, sandwich= Sandwich):
        Agrega un ingrediente al sandwich especificado
    modify_size_to_specific_sandwich(size_command=str, sandwich= Sandwich):
        Cambia el tamaño de un sandwich especificado
    delete_ingredient_to_specific_sandwich(ingredient_command=str, sandwich= Sandwich):
        Remueve un ingrediente del sandwich especificado
    obtain_total_price():
        Retorna el costo total de la orden
    generate_sandwich_options_dict():
        Genera un diccionario con los sandwiches que contiene la orden
    get_number_sandwich_order():
        Retorna la cantidad de sandwiches que contiene la orden
    reset_order():
        Reinicia el atributo order, asignandole una nueva instancia

    """
    
    def __init__(self):
        self.__available_ingredients = []
        self.__available_sizes = []
        self.__order = Order()
        self.__current_sandwich = None
        self.__current_ingredient = None

    def get_order(self):
        """Getter del atributo order"""
        return self.__order
    
    def get_available_ingredients(self):
        """Getter del atributo available_ingredients"""
        return self.__available_ingredients
    
    def get_available_sizes(self):
        """Getter del atributo available_sizes"""
        return self.__available_sizes

    def get_current_sandwich(self):
        """Getter del atributo current_sandwich"""
        return self.__current_sandwich

    def load_available_ingredients(self):
        """Carga los ingregientes al sistema, leyendo el archivo ingrediens.txt"""
        base_path = Path(__file__).parent
        file_path = (base_path / "../config/ingredients.txt").resolve()
        ingredients_list = self.__read_file_lines(file_path)
        for name,command,price in ingredients_list:
            self.__available_ingredients.append(Ingredient(name,command,price))
        
    def load_availables_sizes(self):
        """Carga los tamaños de panes en el sistema, leyendo el atchivp sizes.txt"""
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
        """Retorna el diccionario donde las llaves son comando y los valores
        son los ingrediente que maneja el sistema"""
        ingredients_dict = {}
        for ingredient in self.__available_ingredients :
            ingredients_dict[ingredient.command] = ingredient.name
        return ingredients_dict

    def generate_available_sizes_dict(self) -> dict:
        """Retorna el diccionario donde las llaves son comando y los valores
        son los tamaños de sandwiches que maneja el sistema"""
        sizes_dict = {}
        for size in self.__available_sizes :
            sizes_dict[size.command] = size.name
        return sizes_dict

    def obtain_order_amount(self):
        """Calcula el costo total de la orden"""
        return self.__order.calculate_order_price()

    def set_sandwich_size(self, size_command : str):
        """Asigna un tamaño al sadwich referenciado por el atributo current_sandwich"""
        self.__current_sandwich.size = self.__search_available_size_by_command(size_command)

    def prepare_sandwich(self, size_command : str):
        """Inicia el proceso de creación de sandwiches"""
        self.__current_sandwich = Sandwich()
        self.set_sandwich_size(size_command)
    
    def add_sandwich_to_order(self):
        """Agrega un sandwich a la orden"""
        self.__order.add_sandwich(self.__current_sandwich)

    def add_cloned_sandwich_to_order(self, sandwich_index: int, number_copy: int):
        """Clona un sandwich de la orden tantas veces como indique el parametro number_copy"""
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
        """Agrega un ingrediente al sandwich referenciado por el atributo current_sandwich"""
        self.__current_sandwich.add_ingredient(self.__search_available_ingredient_by_command(ingredient_command))

    def add_ingredient_to_specific_sandwich(self, ingredient_command:str, sandwich: Sandwich):
        """Agrega un ingrediente al sandwich especificado"""
        sandwich.add_ingredient(self.__search_available_ingredient_by_command(ingredient_command))

    def modify_size_to_specific_sandwich(self, size_command:str, sandwich: Sandwich):
        """Cambia el tamaño de un sandwich especificado"""
        sandwich.modify_size(self.__search_available_size_by_command(size_command))
    
    def delete_ingredient_to_specific_sandwich(self, ingredient_command:str, sandwich: Sandwich):
        """Remueve un ingrediente del sandwich especificado"""
        sandwich.remove_ingredient(self.__search_available_ingredient_by_command(ingredient_command))

    def obtain_total_price(self):
        """Retorna el costo total de la orden"""
        return self.__order.calculate_order_price()

    def generate_sandwich_options_dict(self):
        """Genera un diccionario con los sandwiches que contiene la orden"""
        options_dict = { 'q' : 'Salir'}
        for index,sandwich in enumerate(self.__order.get_sandwiches()):
            options_dict[str(index + 1)] = sandwich.get_full_description()
        return options_dict
    
    def get_number_sandwich_order(self):
        """Retorna la cantidad de sandwiches que contiene la orden"""
        return self.__order.get_number_of_sandwiches()
    
    def reset_order(self):
        """Reinicia el atributo order, asignandole una nueva instancia"""
        self.__order = Order()
        self.__current_sandwich = None
        self.__current_ingredient = None
