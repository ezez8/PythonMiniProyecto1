from view.View import View

class CloneSandwichView(View):
    """
    Clase utilizada para representar la vista en la funcionalidad de cloanción de sandwiches

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
    display_options_menu():
        Muesta la lista de ingredientes
    display_finish_message():
        Muestra mensaje de culminación de la operación
    display_request_quantity():
        Muestra mensaje de solicitud de cantidad de sandwiches a ser clonados
    display_empty():
        Muestra mendaje indicando que la funcionalidad esta bloqueda
    """
    def __init__(self, options: dict):
        super().__init__(options)

    def display_main_message(self):
        super().display_main_message()
        print('***'+'{:^56}'.format('CLONAR SÁNDWICH')+'***\n')
    
    def start_display(self):
        self.clean_screen()
        self.display_main_message()
        if len(self.options) == 1:
            self.display_empty()
        else:
            self.display_options_menu()
            self.display_request_message()

    def display_request_message(self):
        print('Indique el número del sándwich que desea clonar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opción válida')
    
    def display_finish_message(self):
        print('\nClonación exitosa\n', end='')
        print('*'*62)
        print('\nPresione ENTER para continuar: ', end='')
    
    def display_request_quantity(self):
        print('Indique cuantas copias del sándwich desea agregar (n > 0): ',end='')

    def display_empty(self):
        print('\n**No existen sandwiches en la orden para clonar**')
        print('\nPresione ENTER para salir: ', end='')

    def display_options_menu(self):
        for command,option in self.options.items():
            if command == 'q':
                continue
            print(f'( {command} )    {option}')
        print(f'( q )    Salir')
        print()           
        