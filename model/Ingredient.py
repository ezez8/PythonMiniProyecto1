class Ingredient(object):
    """
    Clase utilizada para representar los ingredientes disponibles

    ...

    Attributes
    ----------
    name : str
        Nombre del ingrediente
    command : str
        Comando esperado para seleccionar ingrediente
    price : int
        Precio asociado al ingrediente

    Methods
    -------
    name(), name(value=str)
        Getter y setter del atributo name
    command(), command(value=str)
        Getter y setter del atributo command
    price(), price(value=int)
        Getter y setter del atributo price
    
    """

    def __init__(self, name : str, command : str, price : float):
        """
        Parameters
        ----------
        name : str
            Nombre del ingrediente
        command : str
            Comando esperado para seleccionar ingrediente
        price : int
            Precio asociado al ingrediente
        """
        self.name = name
        self.command = command
        self.price = price
    
    @property
    def name(self):
        """Getter del atributo name"""
        return self.__name
    
    @name.setter
    def name(self, value : str):
        """Setter del atributo name"""
        self.__name = value
    
    @property
    def command(self):
        """Getter del atributo command"""
        return self.__command
    
    @command.setter
    def command(self, value : str):
        """Setter del atributo command"""
        self.__command = value

    @property
    def price(self):
        """Getter del atributo price"""
        return self.__price
    
    @price.setter
    def price(self, value : float):
        """Setter del atributo price"""
        if value < 0:
            self.__price = 0
        else:
            self.__price = value
