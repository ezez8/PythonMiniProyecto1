from view.View import View

class WelcomeView(View):
    def __init__(self, options : dict):
        super().__init__(options)

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('MENU PRINCIPAL')+'***\n')

    def display_request_message(self):
        print('Indique la opcion con que desea continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')
    