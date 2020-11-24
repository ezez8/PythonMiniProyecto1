from view.View import View

class ModifySizeView(View):
    def __init__(self, options : dict):
        self.options = options

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('MODIFICAR TAMAÑO DE SÁNDWICH')+'***\n')

    def display_request_message(self):
        print('Indique el tamaño que desea: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción válida')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()

    def display_result(self):
        print(f'\nSe modificó el tamaño satisfactoriamente\n')
        print('*'*62)
    
    def display_new_modification(self):
        print(f'\n¿Desea volver a cambiar el tamaño del sándwich? [s / n]: ', end='') 

    def display_options_menu(self):
        super().display_options_menu()

