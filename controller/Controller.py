from model.Model import Model
from view import View,WelcomeView,OrderView,AddSandwichView,ModifySandwichView,CloneSandwichView,ShowOrderView,AddIngredientView
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
            self.modify_sandwich()
        elif user_input == 'p':
            self.welcome()
        else:
            number_sandwich = self.model.get_number_sandwich_order()
            if number_sandwich > 0:
                self.view.display_request_exit_conformation(number_sandwich)
                confirmation = input()
                if confirmation == 's':
                    self.model.reset_order()
                    return self.welcome()
                else:
                    return self.order_menu()
            return self.welcome()
            
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
        
        final_option = input().lower()
        if final_option == 's':
            return self.add_sandwich()
        return self.order_menu()
    
    def add_ingredient(self):
        order = self.model.get_order()
        self.__initiate_view(ShowOrderView.ShowOrderView(order))
        while True:
            try:
                user_input = input()
                if int(user_input) in range(1,len(order.get_sandwiches())+1):
                    selected_sandwich = int(user_input)-1
                    ingredient_options = self.model.generate_available_ingredients_dict()
                    self.__initiate_view(AddIngredientView.AddIngredientView(order.get_sandwiches()[selected_sandwich],ingredient_options))
                    self.select_ingredient(selected_sandwich)
                else:
                    self.view.display_error_message()
                    self.view.display_request_message()
            except ValueError:
                self.view.display_error_message()
                self.view.display_request_message()
                pass
    
    def select_ingredient(self,selected_sanwich):
        ingredient_options = self.model.generate_available_ingredients_dict()
        self.view.display_options_menu()
        self.view.display_request_ingredient_message()
        user_wish_ingredient = True
        while user_wish_ingredient:
            ingredient_selected_option = input()
            if ingredient_selected_option in ingredient_options:
                self.model.add_ingredient_to_specific_sandwich(ingredient_selected_option,self.model.get_order().get_sandwiches()[selected_sanwich])
                self.view.display_request_ingredient_message()
            elif ingredient_selected_option == '':
                user_wish_ingredient = False
            else:
                self.view.display_error_message()
                self.view.display_request_ingredient_message()
        self.view.display_result()
        self.view.display_new_modification()
        user_input = input()
        if user_input == 's':
            self.modify_sandwich()
        else:
            self.order_menu()


    def delete_ingredient(self):
        print("pruebas")

    def modify_sandwich(self):
        options = {'a' : 'Agregar Ingrediente','q' : 'Quitar Ingrediente','m' : 'Modificar Tamaño','s' : 'Salir'}
        order = self.model.get_order()
        self.__initiate_view(ModifySandwichView.ModifySandwichView( options))
        user_input = input()
        if user_input == 'a':
            self.add_ingredient()
        elif user_input == 'q':
            self.delete_ingredient()
        elif user_input == 'm':
            self.welcome()
        elif user_input == 's':
            self.order_menu()
        else:
            self.order_menu()
            

    def clone_sandwich(self):
        sandwich_options = self.model.generate_sandwich_options_dict()
        self.__initiate_view(CloneSandwichView.CloneSandwichView(sandwich_options))

        if len(sandwich_options) == 1:
            input()
        else:
            user_input = self.__read_option(sandwich_options)

            if user_input == 'q':
                return self.order_menu()
            else:
                sandwich_index = int(user_input) - 1
                number_copy =  None
                while not number_copy:
                    self.view.display_request_quantity()
                    user_input = input()
                    if user_input.isdigit():
                        number_copy = int(user_input) if int(user_input) > 0 else None
                    else:
                        self.view.display_error_message()
                self.model.add_cloned_sandwich_to_order(sandwich_index,number_copy)
                self.view.display_finish_message()
                input()
        return self.order_menu()

    def end_program(self):
        exit()



