from view.View import View
from model import *

class ShowOrderView(View):
    def __init__(self, order: Order):
        self.__order = order

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Orden de Sandwich: \n')

    def display_request_message(self):
        print('Indique el sandwich que desea modificar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')

    def display_empty(self):
        print('=> No hay ordenes existentes para modificar \n')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()
        self.display_order()
        self.display_request_message()

    def display_order(self):
        count = 1
        order = self.__order.get_sandwiches()
        for sandwich in order:
            print(f'( {count} ) sandwich {sandwich.get_full_description()}\n')
            count += 1
