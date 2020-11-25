from view.View import View

class DeleteIngredientView(View):
    """
    Clase utilizada para representar la vista en la funcionalidad de remover ingredientes

    ...
    Superclass
    ----------
    View

    Attributes
    ----------
    

    Methods
    -------
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
    display_result():
        Muesta mensaje de confirmación de exito de la operación
    display_new_modification():
        Muesta mensaje de solicitud de realizad de nuevo la operación
    display_negation_message():
        Muesta mensaje de solicitud de permiso para continuar
    display_empty():
        Muestra mendaje indicando que la funcionalidad esta bloqueda

    """
    def __init__(self, ingredient_options: dict):
        super().__init__(ingredient_options)

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('REMOVER INGREDIENTE A UN SÁNDWICH')+'***\n')

    def display_request_message(self):
        print('Indique el ingrediente que desea eliminar: ', end='')

    def display_negation_message(self):
        print('\nPresione ENTER para salir: ', end='')

    def display_empty(self):
        print('**No hay ingredientes en el sándwich en este momento**\n', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción válida')

    def display_request_ingredient_message(self):
        print('Indique ingrediente (enter para terminar): ', end='')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()

    def display_options_menu(self):
        print('\nLista de Ingredientes:\n')
        super().display_options_menu()

    def display_result(self):
        print(f'\nSe eliminó el ingrediente satisfactoriamente\n')
        print('*'*62) 

    def display_new_modification(self):
        print(f'\n¿Desea eliminar otro ingrediente del sándiwch? [s / n]: ', end='') 

