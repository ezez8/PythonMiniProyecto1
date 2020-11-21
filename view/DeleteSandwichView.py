from view.View import View
from model.Order import Order

class DeleteSandwichView(View):
    def __init__(self, order: Order):
        self.__order = order

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Eliminar Sandwich\n')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()
    
    def display_request_message(self):
        print('Indique una opcion para continuar (ENTER para volver al menu): ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')

    def display_empty(self):
        print('No hay Sandwiches ordenados en este momento\n')

    def display_empty_msg(self):
        print('Presione ENTER para salir: ', end='')

    def display_finish_message(self):
        print('Presione ENTER para continuar: ', end='')

    def display_order(self ):
        x = self.__order.get_sandwiches()
        cont = 1
        print('lista de sandwiches ordenadas\n')
        for sandwich in x:
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
            print(f'({cont}) Sandwich {sandwich.size.name}{ingredients_section}\n')
            cont += 1