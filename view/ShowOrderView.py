from view.View import View
from model import *

class ShowOrderView(View):
    """
    Clase utilizada para representar la lista de sandwiches que contiene la orden

    ...
    Superclass
    ----------
    View

    Attributes
    ----------
    order : Order
        Contiene información del detalle de la orden

    Methods
    -------
    display_main_message():
        Muestra el encabezado de la vista
    display_request_message():
        Muestra el mensaje de solicitud de ingreso de opción
    display_error_message():
        Muestra mensaje de error al ingresar una opción inválidaón
    start_display():
        Inicia la vista
    display_empty():
        Muestra mendaje indicando que la funcionalidad esta bloqueda
    display_back_message():
        Muestra opción de retornar al menu de modificación de ordenes
    display_order()
        Muertra la lista de sandwiches que conforman la orden

    """
    def __init__(self, order: Order):
        self.__order = order

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('SANDWICH(ES) EN LA ORDEN')+'***\n')

    def display_request_message(self):
        print('Indique el sandwich que desea modificar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción válida')

    def display_empty(self):
        print('=> No hay ordenes existentes para modificar \n')

    def display_back_message(self):
        print('( v ) Volver al menu de modificar\n')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()
        self.display_order()
        self.display_back_message()
        self.display_request_message()

    def display_order(self):
        count = 1
        order = self.__order.get_sandwiches()
        for sandwich in order:
            print(f'( {count} ) Sándwich {sandwich.get_full_description()}')
            count += 1
