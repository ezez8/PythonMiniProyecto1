from model.Model import Model
from view import View,WelcomeView,OrderView,AddSandwichView,CloneSandwichView
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
        self.__initiate_view(WelcomeView.WelcomeView(options))

        user_input = self.__read_option(options)

        if user_input == 'o':
            self.order_menu()
        else:
            self.end_program()
        
    def order_menu(self):
        options = {'a' : 'Agregar Sandwich','e' : 'Eliminar Sandwich','c' : 'Clonar Sandwich','m' : 'Modificar Sandwich','p' : 'Pagar','q' : 'Salir'}
        self.__initiate_view(OrderView.OrderView(options))

        user_input = self.__read_option(options)

        if user_input == 'a':
            self.add_sandwich()
        elif user_input == 'e':
            self.welcome()
        elif user_input == 'c':
            self.clone_sandwich()
        elif user_input == 'm':
            self.welcome()
        elif user_input == 'p':
            self.welcome()
        else:
            self.welcome()
    
    def add_sandwich(self):
        ingredient_options = self.model.generate_available_ingredients_dict()
        size_options = self.model.generate_available_sizes_dict()
        self.__initiate_view(AddSandwichView.AddSandwichView(ingredient_options,size_options))

        size_selected_option = self.__read_option(size_options)

        self.model.prepare_sandwich(size_selected_option)

        self.view.display_options_menu()
        self.view.display_request_ingredient_message()

        user_wish_ingredient = True
        while user_wish_ingredient:
            ingredient_selected_option = input()
            if ingredient_selected_option in ingredient_options:
                self.model.add_ingredient_to_sandwich(ingredient_selected_option)
                self.view.display_request_ingredient_message()
            elif ingredient_selected_option == '':
                user_wish_ingredient = False
            else:
                self.view.display_error_message()
                self.view.display_request_ingredient_message()

        self.view.display_created_sandwich(self.model.get_current_sandwich())
        self.model.add_sandwich_to_order()
        self.view.display_finish_message()
        input()
        self.order_menu()

    def clone_sandwich(self):
        order = self.model.get_order()
        self.__initiate_view(CloneSandwichView.CloneSandwichView(order))
        self.view.display_request_message()
        user_want_clone = True

        while user_want_clone:
            selected_option = input()
            cont = len(self.model.get_order().get_sandwiches())
            if int(selected_option) > cont or int(selected_option) < 0:
                self.view.display_error_message()
            else:
                sandwich = self.model.get_order().get_sandwiches()[int(selected_option) - 1]
                self.model.add_cloned_sandwich_to_order(sandwich)
                user_want_clone = False
        self.view.display_finish_message()
        input()
        self.order_menu()

                
                
                



                    
                


        
        

    def end_program(self):
        exit()



