from view.View import View
from model.Sandwich import Sandwich
from model.Size import Size

class AddSandwichView(View):
    def __init__(self, ingredient_options: dict, size_options: dict):
        self.size_options = size_options
        super().__init__(ingredient_options)
    
    def display_size_options(self):
        print('\nTamaños diponibles :\n')
        for command,name in self.size_options.items():
            print(f'( {command} )    {name}')
        print()

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('CREACION DE SANDWICH')+'***\n')
    
    def start_display(self):
        self.clean_screen()
        self.display_main_message()
        self.display_size_options()
        self.display_request_message()

    def display_request_message(self):
        print('Indique una opcion para continuar: ', end='')
    
    def display_request_ingredient_message(self):
        print('Indique ingrediente (enter para terminar): ', end='')
    
    def display_finish_message(self):
        print('Presione ENTER para continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')

    def display_options_menu(self):
        print('\nLista de Ingredientes:\n')
        super().display_options_menu()
    
    def display_created_sandwich(self, sandwich : Sandwich):
        print(f'\nUsted seleccionó un sándwich {sandwich.get_full_description()}\n')
        print(f'Subtotal a pagar por el sándwich {sandwich.get_small_description()}: {sandwich.calculate_price() : .2f}\n')
        print('*'*62)
        print('\n¿Desea agregar otro sándwich a la orden [s / n]?: ',end='')

    