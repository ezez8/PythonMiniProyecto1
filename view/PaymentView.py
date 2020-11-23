from view.View import View
from model.Order import Order

class PaymentView(View):
    def __init__(self, order: Order):
        self.__order = order

    def start_display(self):
        self.clean_screen()
        self.display_main_message()
    
    def display_request_message(self):
        print('Indique una opcion para continuar (ENTER para volver al menu): ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Pago Sandwich\n')

    def display_factura(self):
        print('*'*62)
        print('*'+'{:^60}'.format('FACTURA')+'*')
        print('*'*62)
        sandwiches_list = [(s.get_full_description(),s.calculate_price()) for s in self.__order.get_sandwiches()]
        for sandwich_des, price in sandwiches_list:            
            print('*{sandwich_des:31.31}...{price:>25.2f}$*'.format(sandwich_des=sandwich_des, price=price))
        print('*'*62)
        print('*Total{total:>54.2f}$*'.format(total=self.__order.calculate_order_price()))
        print('*'*62+'\n')

    def order_empty(self):
        print('**La orden esta vacia**')

    def display_payment_confirmation(self):
        print('Desea efectuar el pago? [s / n]: ', end='')

    def display_success_payment(self):
        print('\n**Gracias por su compra. Vuelva pronto**')

    def display_finish_message(self):
        print('\nPresione ENTER para continuar: ', end='')