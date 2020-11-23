from view.View import View
from model import *

class ModifySizeView(View):
    def __init__(self, options : dict):
        self.options = options

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Modificacion de sandwich\n')

    def display_request_message(self):
        print('Indique el tamaño que desea: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()

    def display_result(self):
        print(f'\nSe modifico el tamaño satisfactoriamente\n')
        print('************************************')
    
    def display_new_modification(self):
        print(f'\n¿Desea volver a cambiar el tamaño del sandwich? [s / n]: ', end='') 

    def display_options_menu(self):
        super().display_options_menu()

