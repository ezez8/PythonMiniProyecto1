from view.View import View
from model.Order import Order

class PaymentView(View):
    """
    Clase utilizada para representar la vista en la funcionalidad de efectuar pago de orden

    ...
    Superclass
    ----------
    View

    Attributes
    ----------
    Order:
        Contiene los datos de la orden del cliente

    Methods
    -------
    display_main_message():
        Muestra el encabezado de la vista
    display_request_message():
        Muestra el mensaje de solicitud de ingreso de opción
    display_error_message():
        Muestra mensaje de error al ingresar una opción inválida
    display_finish_message():
        Muestra mensaje de culminación de la operación
    display_payment_confirmation():
        Muestra mensaje solicitando permiso para efectuar el pago
    start_display():
        Inicia la vista
    display_factura():
        Imprime la factura asociada a la orden
    order_empty():
        Muestra mendaje indicando que la funcionalidad esta bloqueda
    display_success_payment()
        Muestra mesjade de exito de la operación

    """
    def __init__(self, order: Order):
        self.__order = order

    def start_display(self):
        self.clean_screen()
        self.display_main_message()
    
    def display_request_message(self):
        print('Indique una opción para continuar (ENTER para volver al menu): ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción válida')

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('PAGO DE ORDENES')+'***\n')

    def display_factura(self):
        print('*'*62)
        print('*'+'{:^60}'.format('FACTURA')+'*')
        print('*'*62)
        sandwiches_list = [(s.get_full_description(),s.calculate_price()) for s in self.__order.get_sandwiches()]
        for sandwich_des, price in sandwiches_list:            
            print('*{sandwich_des:41.31}...{price:>15.2f}$*'.format(sandwich_des=sandwich_des, price=price))
        print('*'*62)
        print('*{total_str:41.31}...{total_amount:>15.2f}$*'.format(total_str='Total', total_amount=self.__order.calculate_order_price()))
        print('*'*62+'\n')

    def order_empty(self):
        print('**La orden esta vacía**')

    def display_payment_confirmation(self):
        print('¿Desea efectuar el pago? [s / n]: ', end='')

    def display_success_payment(self):
        print('\n**Gracias por su compra. Vuelva pronto**')

    def display_finish_message(self):
        print('\nPresione ENTER para continuar: ', end='')