from view.View import View
from model import *

class DeleteIngredientView(View):
    def __init__(self, ingredient_options: dict):
        super().__init__(ingredient_options)

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Eliminar ingrediente a un sandwich\n')

    def display_request_message(self):
        print('Indique el ingrediente que desea eliminar: ', end='')

    def display_negation_message(self):
        print('El sandwich no puede tener menos de un ingrediente (ENTER para volver al menu anterior)', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')

    def display_request_ingredient_message(self):
        print('Indique ingrediente (enter para terminar): ', end='')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()

    def display_options_menu(self):
        print('\nLista de Ingredientes:\n')
        super().display_options_menu()

    def display_result(self):
        print(f'\nSe elimino el ingrediente satisfactoriamente\n')
        print('************************************')

    def display_new_modification(self):
        print(f'\n¿Desea seguir modificando el sandwich? [s / n]: ', end='') 

