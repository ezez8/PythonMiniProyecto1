class DeleteSandwichView(View):
    def __init__(self, options : dict):
        self.options = options

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Eliminar Sandwich\n')
    
    def display_request_message(self):
        print('Indique una opcion para continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')