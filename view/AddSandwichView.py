from view.View import View
from model.Sandwich import Sandwich

class AddSandwichView(View):
    """
    Clase utilizada para representar la vista en la funcionalidad de creación de sandwiches

    ...
    Superclass
    ----------
    View

    Attributes
    ----------
    size_options : dict
        Diccionario de tamaño de sandwiches disponibles

    Methods
    -------
    display_size_options():
        Muestra las opciones de tamaño de sandwiches disponibles
    display_main_message():
        Muestra el encabezado de la vista
    display_request_message():
        Muestra el mensaje de solicitud de ingreso de opción
    display_error_message():
        Muestra mensaje de error al ingresar una opción inválida
    display_request_ingredient_message():
        Muestra mensaje de solicitud de ingreso de ingredientes
    start_display():
        Inicia la vista
    display_options_menu():
        Muesta la lista de ingredientes
    display_finish_message():
        Muestra mensaje de culminación de la operación
    display_created_sandwich():
        Muestra mensaje de exito en creación de sandwich
    """
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
        print('***'+'{:^56}'.format('CREACIÓN DE SÁNDWICH')+'***\n')
    
    def start_display(self):
        self.clean_screen()
        self.display_main_message()
        self.display_size_options()
        self.display_request_message()

    def display_request_message(self):
        print('Indique una opción para continuar: ', end='')
    
    def display_request_ingredient_message(self):
        print('Indique ingrediente (ENTER para terminar): ', end='')
    
    def display_finish_message(self):
        print('Presione ENTER para continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción válida')

    def display_options_menu(self):
        print('\nLista de Ingredientes:\n')
        super().display_options_menu()
    
    def display_created_sandwich(self, sandwich : Sandwich):
        print(f'\nUsted seleccionó un sándwich {sandwich.get_full_description()}\n')
        print(f'Subtotal a pagar por el sándwich {sandwich.get_small_description()}: {sandwich.calculate_price() : .2f}\n')
        print('*'*62)
        print('\n¿Desea agregar otro sándwich a la orden [s / n]?: ',end='')

    