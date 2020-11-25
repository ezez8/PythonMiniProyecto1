from model.Sandwich import Sandwich

class Order(object):
    """
    Clase utilizada para representar la orden generada por el cliente

    ...

    Attributes
    ----------
    sandwiches : list
        Listado de sandwiches que contiene la orden

    Methods
    -------
    get_sandwiches(), set_sandwiches(sandwiches=list)
        Getter del atributo sandwiches
    set_sandwiches(sandwiches=list):
        Setter del atributo sandwiches
    add_sandwich(sandwich=Sandwich):
        Agrega un sandwich a la orden
    remove_sandwich(id=int):
        Elimina un sandwich de la orden
    calculate_order_price():
        Retorna el costo total de la orden
    get_number_of_sandwiches():
        Devuelve la cantidad de sandwiches que contiene la orden
    
    """

    def __init__(self):
        self.__sandwiches = []
    
    def get_sandwiches(self):
        """Getter del atributo sandwiches"""
        return self.__sandwiches
    
    def set_sandwiches(self, sandwiches : list):
        """Setter del atributo sandwiches"""
        self.__sandwiches = sandwiches
    
    def add_sandwich(self, sandwich : Sandwich):
        """Getter del atributo sandwiches"""
        self.__sandwiches.append(sandwich)
    
    def remove_sandwich(self, id : int):
        """Elimina un sandwich de la orden segun el indice con base 1"""
        del self.__sandwiches[id-1]

    def calculate_order_price(self):
        """Retorna el precio de la orden, acumulando el precio de cada sandwich"""
        price = 0
        for sandwich in self.__sandwiches:
            price += sandwich.calculate_price()
        return price
    
    def get_number_of_sandwiches(self):
        """Retorna la candidad de sandwiches existentes en la orden"""
        return len(self.__sandwiches)
