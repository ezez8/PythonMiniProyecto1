from view.View import View
from model.Order import Order

class DeleteSandwichView(View):
    def __init__(self, order: Order):
        self.__order = order

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('ELIMINAR SANDWICH')+'***\n')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()
    
    def display_request_message(self):
        print('\nIndique el numero de Sandwich que desea eliminar(ENTER para volver al menu): ', end='')

    def display_error_message(self):
        print('\n**Debe ingresar una opcion valida**')

    def display_empty(self):
        print('\n**No hay Sandwiches ordenados en este momento**\n', end='')

    def display_finish_message(self):
        print('\nPresione ENTER para salir: ', end='')

    def display_continue_message(self):
        print('\nPresione ENTER para continuar: ', end='')

    def display_success_message(self):
        print('\n**Sandwich eliminado satisfactoriamente**')        

    def display_delete_other_confirmation(self):
        print('\nDesea eliminar otro Sandwich [s / n]: ', end='')

    def display_order(self ):
        print()
        sandwiches_list = self.__order.get_sandwiches()
        opcions_list = list(zip([i for i in range(1, len(sandwiches_list)+1)], [s.get_full_description() for s in sandwiches_list]))
        for count, sandwich_full_des in opcions_list:
            print(f'( {count:0>{len(str(len(sandwiches_list)))}} )    {sandwich_full_des}')