from view.View import View

class ModifySandwichView(View):
    """
    Clase utilizada para representar la vista de la funcionalidad de modificar de ingredientes

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
        Muestra mensaje de error al ingresar una opción inválidaón
    start_display():
        Inicia la vista
    display_empty():
        Muestra mendaje indicando que la funcionalidad esta bloqueda
    display_order()
        Muertra la lista de sandwiches que conforman la orden

    """
    def __init__(self, options : dict):
        super().__init__(options)

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('MODIFICAR SÁNDWICH')+'***\n')

    def display_request_message(self):
        print('Indique la opción con que desea continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción valida')

    def display_empty(self):
        print('**No existen sandwiches en la orden para modificar**\n', end='')
        print('\nPresione ENTER para salir: ', end='')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()

    def display_order(self):
        count = 1
        order = self.__order.get_sandwiches()
        for sandwich in order:
            print(f'( {count} ) Sándwich {sandwich.get_full_description()}\n')
            count += 1
