from view.View import View

class OrderView(View):
    def __init__(self, options: dict):
        super().__init__(options)

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Creacion de ordenes:\n')

    def display_request_message(self):
        print('Indique la opcion con que desea continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')
    
    def display_request_exit_conformation(self, number_of_sandwiches: int):
        plural = 'es' if number_of_sandwiches > 1 else ''
        print(f'Su orden contiene ( {number_of_sandwiches} ) sándwich{plural} y no ha sido cancelada')
        print('Si decide salir en este momento la informacion se borrara del sistema')
        print('¿Desea salir del sistema [s / n]?: ',end='')    
