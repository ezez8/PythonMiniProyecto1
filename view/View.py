from abc import ABC, abstractmethod
from os import system, name
class View(ABC):
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

        