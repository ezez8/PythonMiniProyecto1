from model.Model import Model
from view import *
from sys import exit

class Controller(object):

    def __init__(self):
        self.view = None
        self.model = None
    
    @property
    def view(self):
        return self.__view
    
    @view.setter
    def view(self, value : View):
        self.__view = value
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value : Model):
        self.__model = value
    
    def start(self):
        self.model = Model()
        self.model.load_available_ingredients()
        self.model.load_availables_sizes()
        self.welcome()
    
    def __read_option(self, options: dict) ->  str:
        user_input = ''
        invalid_option_select = True
        while invalid_option_select:
            user_input = input().lower()
            invalid_option_select = user_input not in options
            if invalid_option_select:
                self.view.display_error_message()
                self.view.display_request_message()
        return user_input
    
    def __initiate_view(self, view : View):
        self.view = view
        self.view.clean_screen()
        self.view.start_display()
    
    def welcome(self):
        options = {'o' : 'Ordenar', 'q' : 'Salir'}
        self.__initiate_view(WelcomeView(options))

        user_input = self.__read_option(options)

        if user_input == 'o':
            self.order_menu()
        else:
            self.end_program()
        
    def order_menu(self):
        options = {'a' : 'Agregar Sandwich','c' : 'Clonar Sandwich','m' : 'Modificar Sandwich','p' : 'Pagar','q' : 'Salir'}
        self.__initiate_view(OrderView(options))

        user_input = self.__read_option(options)

        if user_input == 'a':
            self.welcome()
        elif user_input == 'c'
            self.welcome()
        elif user_input == 'm'
            self.welcome()
        elif user_input == 'p'
            self.welcome()
        else:
            self.welcome()

    def end_program(self):
        exit()



