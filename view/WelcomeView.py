from View import View

class WelcomeView(View):
    def __init__(self):
        super().__init__({'o' : 'Ordenar', 'q' : 'Salir'})

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Menu principal:\n')

    def display_request_message(self):
        print('Indique la opcion con que desea continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')
    