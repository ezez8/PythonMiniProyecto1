from abc import ABC, abstractmethod
from os import system, name
class View(ABC):
    """
    Clase Abstracta utilizada como base para las vistas de la aplicación

    ...
    Superclass
    ----------
    ABC

    Attributes
    ----------
    options : dict
        Contiene la lista de comondos válidos relacionados con la vista

    Methods
    -------
    display_main_message():
        Método abstracto para encabezado de la vista
    display_request_message():
        Método abstracto para mostrar el mensaje de solicitud de ingreso de opción
    display_error_message():
        Método abstracto para mostrar mensaje de error al ingresar una opción inválidaón
    start_display():
        Inicia la vista
    display_empty():
        Muestra mendaje indicando que la funcionalidad esta bloqueda
    display_back_message():
        Muestra opción de retornar al menu de modificación de ordenes
    display_options_menu()
        Muestra la lista de opciones de comandos válidos de la vista
    clean_screen():
        Limpia el terminal, en so posix y windows

    """
    def __init__(self, options : dict):
        self.options = options

    @abstractmethod
    def display_main_message(self):
        pass
    
    @abstractmethod
    def display_request_message(self):
        pass

    @abstractmethod
    def display_error_message(self):
        pass
    
    def display_options_menu(self):
        for command,option in self.options.items():
            print(f'( {command} )    {option}')
        print()
    
    def display_main_message(self):
        print('*'*62)
        print('*'+'{:^60}'.format('SANDWICHES UCAB')+'*')
        print('*'*62)
        print()
    
    def start_display(self):
        self.clean_screen()
        self.display_main_message()
        self.display_options_menu()
        self.display_request_message()

    def clean_screen(self):
        #windows
        if name == 'nt':
            system('cls') 
        #mac and linux 
        else: 
            system('clear')

        