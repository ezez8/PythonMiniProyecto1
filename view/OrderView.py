from view.View import View

class OrderView(View):
    """
    Clase utilizada para representar la lista de funcionalidades de la creación de ordenes

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
    display_request_exit_conformation():
        Muestra mensje solicitando confirmación de salida del menu de opciones

    """
    def __init__(self, options: dict):
        super().__init__(options)

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('CREACIÓN DE ORDENES')+'***\n')

    def display_request_message(self):
        print('Indique la opción con que desea continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción válida')
    
    def display_request_exit_conformation(self, number_of_sandwiches: int):
        plural = 'es' if number_of_sandwiches > 1 else ''
        print(f'Su orden contiene ( {number_of_sandwiches} ) sándwich{plural} y no ha sido cancelada')
        print('Si decide salir en este momento la información se borrara del sistema')
        print('¿Desea salir del sistema [s / n]?: ',end='')    
