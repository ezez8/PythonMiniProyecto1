from view.View import View

class WelcomeView(View):
    """
    Clase utilizada para representar la vista principal de la apliación

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

    """
    def __init__(self, options : dict):
        super().__init__(options)

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('MENU PRINCIPAL')+'***\n')

    def display_request_message(self):
        print('Indique la opción con que desea continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción válida')
    