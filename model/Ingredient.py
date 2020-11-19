class Ingredient(object):

    def __init__(self, name : str, command : str, price : float):
        self.name = name
        self.command = command
        self.price = price
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value : str):
        self.__name = value
    
    @property
    def command(self):
        return self.__command
    
    @command.setter
    def command(self, value : str):
        self.__command = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value : float):
        if value < o:
            self.__price = 0
        else:
            self.__price = value
