from view.View import View
from model.Sandwich import Sandwich
from model.Size import Size

class AddSandwichView(View):
    def __init__(self, ingredient_options: dict, size_options: dict):
        self.size_options = size_options
        super().__init__(ingredient_options)
    
    def display_size_options(self):
        print('\nTamaños :')
        for command,name in self.size_options.items():
            print(f'( {command} )    {name}')
        print()

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Creacion de sandwich\n')
    
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
        size_section = sandwich.size.name

        ingredients_list = [ingredient.name for ingredient in sandwich.ingredients_list]
        number_of_ingredients = len(ingredients_list)
        ingredients_section = ''
        if  number_of_ingredients == 0:
            ingredients_section = ''
        elif number_of_ingredients == 1:
            ingredients_section = f' con {ingredients_list[0]}'
        else:
            first_part = ', '.join(ingredients_list[0:-1])
            last_part = ingredients_list[-1]
            ingredients_section = f' con {first_part} y {last_part}'
        
        print(f'Usted seleccionó un sándwich {size_section}{ingredients_section}\n')
        print(f'Subtotal a pagar por el sándwich {size_section}: {sandwich.calculate_price() : .2f}')
        print('************************************')

    