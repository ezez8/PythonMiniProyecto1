from view.View import View

class AddSandwichView(View):
    def __init__(self, ingredient_options: dict, size_options: dict):
        self.size_options = size_options
        super().__init__(options)
    
    def display_size_options(self):
        print('\nTamaños :')
        for command,option in self.size_options.items():
            print(f'( {command} )    {option}')

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Creacion de sandwich\n')
    
    def start_display(self):
        self.display_main_message()
        self.display_size_options()
        self.display_request_message()

    def display_request_message(self):
        print('Indique una opcion para continuar: ', end='')
    
    def display_request_ingredient_message(self):
        print('\nIndique ingrediente (enter para terminar): ', end='')
    
    def display_finish_message(self):
        print('Presione ENTER para continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')
    