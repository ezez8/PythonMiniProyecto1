from view.View import View

class ModifySizeView(View):
    """
    Clase utilizada para representar la vista en la funcionalidad de modificación de tamaño de sandwiches

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
    start_display():
        Inicia la vista
    display_result():
        Muestra mensaje indicando que la operación de modificación se ha completado exitosamente

    """
    def __init__(self, options : dict):
        super().__init__(options)

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('MODIFICAR TAMAÑO DE SÁNDWICH')+'***\n')

    def display_request_message(self):
        print('Indique el tamaño que desea: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción válida')

    def start_display(self):
        self.clean_screen()
        self.display_main_message()

    def display_result(self):
        print(f'\nSe modificó el tamaño satisfactoriamente\n')
        print('*'*62)
    
    def display_new_modification(self):
        print(f'\n¿Desea volver a cambiar el tamaño del sándwich? [s / n]: ', end='') 
