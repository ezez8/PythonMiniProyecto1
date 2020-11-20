from view.View import View
from model.Sandwich import Sandwich
from model.Size import Size

class ModyfiSandwichView(View):
    def __init__(self, options: dict):
        super().__init__(options)

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Modificacion de sandwich\n')

    def display_request_message(self):
        print('Indique una opcion para continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()
        self.display_option()
        self.display_request_message()

    def display_option(self):
        super().display_options_menu()