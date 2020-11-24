from view.View import View
from model.Order import Order

class DeleteSandwichView(View):
    def __init__(self, order: Order):
        self.__order = order

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('ELIMINAR SÁNDWICH')+'***\n')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()
    
    def display_request_message(self):
        print('\nIndique el número de Sándwich que desea eliminar: ', end='')

    def display_error_message(self):
        print('\n**Debe ingresar una opción válida**')

    def display_empty(self):
        print('\n**No existen sandwiches en la orden para eliminar**\n', end='')

    def display_finish_message(self):
        print('\nPresione ENTER para salir: ', end='')

    def display_continue_message(self):
        print('\nPresione ENTER para continuar: ', end='')

    def display_success_message(self):
        print('\nSándwich eliminado satisfactoriamente')
        print('*'*62)       

    def display_delete_other_confirmation(self):
        print('\n¿Desea eliminar otro sándwich? [s / n]: ', end='')

    def display_order(self ):
        print()
        sandwiches_list = self.__order.get_sandwiches()
        opcions_list = list(zip([i for i in range(1, len(sandwiches_list)+1)], [s.get_full_description() for s in sandwiches_list]))
        for count, sandwich_full_des in opcions_list:
            print(f'( {count:0>{len(str(len(sandwiches_list)))}} )    {sandwich_full_des}')
        print(f'( q )    Salir')