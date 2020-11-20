from view.View import View
from model.Order import Order


class CloneSandwichView(View):
    def __init__(self, order: Order):
        self.__order = order

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Clonar sandwich:\n')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()
        self.display_order()

    def display_request_message(self):
        print('Indique el numero del sandwich que desea clonar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')
    
    def display_finish_message(self):
        print('\n************************************')
        print('Clonacion exitosa\n', end='')
        print('\nPresione ENTER para continuar: ', end='')

    def display_empty(self):
        print('\nNo se encuentran sandwiches en la orden para clonar, favor agregar un sandwich primer, (presione ENTER para volver)\n')


    def display_order(self ):
        
        x = self.__order.get_sandwiches()
        cont = 1
        print('lista de sandwiches ordenas')
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
            
        