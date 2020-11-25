from model.Model import Model
from view import View,WelcomeView,OrderView,AddSandwichView,ModifySandwichView,CloneSandwichView,ShowOrderView,AddIngredientView,DeleteSandwichView,PaymentView,DeleteIngredientView,ModifySizeView
from sys import exit

class Controller(object):
    """
    Clase utilizada para representar el controlador de patron MVC

    ...

    Attributes
    ----------
    view : View
        Vista actual del sistema
    model: Model
        Modelo del patron MVC

    Methods
    -------
    view():
        Getter del atributo view
    view( value = View):
        Setter del atributo view
    model():
        Getter del atributo model
    model( value = Model):
        Setter del atributo model
    start():
        Inicia la aplicacion, cargo la vista de bienvenida y los parametros de configuración al modelo
    welcome():
        Controlo las funcionalidades de la pantalla de bienvenida
    order_menu():
        Controla las funcionalidades del menu de creación de ordenes
    add_sandwich():
        Contrala la funcionalidad de agregar sandwiches a la orden
    add_ingredient():
        Contola la funcionalidad de agregar ingredientes a los sandwiches
    select_ingredient(selected_sanwich):
        Controla la funcionalidad de seleccion de ingredientes
    selected_sandwich_disply():
        Controla la funcionalidad de selección de sandwiches
    delete_ingredient( mod_sandwich):
        Controla la funcionalidad de remover ingredientes
    modify_size():
        Controla la funcionalidad de modificación de tamaño de sandwiches
    change_size( selected_sandwich, size_options):
        Función auxiliar en la funcionalidad de modificación de tamaño de sandwiches
    modify_sandwich():
        Controla las funcionalidades del menu de seleccion de sandwich
    clone_sandwich():
        Controla la funcionalidad de clonar sanwiches
    end_program():
        Finaliza el programa
    delete_sandwich():
        Controla la funcionalidad de eliminar sandwiches de la orden
    payment():
        Controla la funcionalidad de pagos de ordenes
    """

    def __init__(self):
        self.view = None
        self.model = None
    
    @property
    def view(self):
        """Getter del atributo view"""
        return self.__view
    
    @view.setter
    def view(self, value : View):
        """Setter del atributo view"""
        self.__view = value
    
    @property
    def model(self):
        """Getter del atributo model"""
        return self.__model
    
    @model.setter
    def model(self, value : Model):
        """Setter del atributo model"""
        self.__model = value
    
    def start(self):
        """Inicia la aplicacion, cargo la vista de bienvenida y los parametros de configuración al modelo"""
        self.model = Model()
        self.model.load_available_ingredients()
        self.model.load_availables_sizes()
        return self.welcome()
    
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
        self.view.start_display()
    
    def welcome(self):
        """Controlo las funcionalidades de la pantalla de bienvenida"""
        options = {'c' : 'Crear nueva orden', 'q' : 'Salir'}
        self.__initiate_view(WelcomeView.WelcomeView(options))

        user_input = self.__read_option(options)

        if user_input == 'c':
            return self.order_menu()
        else:
            return self.end_program()
        
    def order_menu(self):
        """Controlo las funcionalidades la creción de ordernes"""
        options = {'a' : 'Agregar Sandwich','e' : 'Eliminar Sandwich','c' : 'Clonar Sandwich','m' : 'Modificar Sandwich','p' : 'Pagar','q' : 'Salir'}
        self.__initiate_view(OrderView.OrderView(options))

        user_input = self.__read_option(options)

        if user_input == 'a':
            return self.add_sandwich()
        elif user_input == 'e':
            return self.delete_sandwich()
        elif user_input == 'c':
            return self.clone_sandwich()
        elif user_input == 'm':
            return self.modify_sandwich()
        elif user_input == 'p':
            return self.payment()
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
        """Controlo la funcionalidad de agregar sadwiches"""
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
        """Controlo las funcionalidad de agragar ingredients"""
        order = self.model.get_order()
        self.__initiate_view(ShowOrderView.ShowOrderView(order))
        while True:
            try:
                user_input = input()
                if user_input == 'v':
                    return self.modify_sandwich()
                elif int(user_input) in range(1,len(order.get_sandwiches())+1):
                    selected_sandwich = int(user_input)-1
                    ingredient_options = self.model.generate_available_ingredients_dict()
                    self.__initiate_view(AddIngredientView.AddIngredientView(ingredient_options))
                    return self.select_ingredient(selected_sandwich)
                else:
                    self.view.display_error_message()
                    self.view.display_request_message()
            except ValueError:
                self.view.display_error_message()
                self.view.display_request_message()
    
    def select_ingredient(self,selected_sanwich):
        """Controlo las funcionalidad de sellción de ingredientes"""
        ingredient_options = self.model.generate_available_ingredients_dict()
        self.view.start_display()
        self.view.display_options_menu()
        self.view.display_request_message()
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
            return self.select_ingredient(selected_sanwich)
        else:
            return self.modify_sandwich()

    def selected_sandwich_disply(self):
        """Controlo las funcionalidad de seleccion de sandwiches"""
        order = self.model.get_order()
        self.__initiate_view(ShowOrderView.ShowOrderView(order))
        while True:
            user_input = input()
            try:
                if user_input == 'v':
                    return self.modify_sandwich()
                elif int(user_input) in range(1,len(order.get_sandwiches())+1):
                    selected_sandwich = int(user_input)-1
                    mod_sandwich = self.model.get_order().get_sandwiches()[selected_sandwich]
                    return self.delete_ingredient(mod_sandwich)
                else:
                    self.view.display_error_message()
                    self.view.display_request_message()
            except ValueError:
                self.view.display_error_message()
                self.view.display_request_message()            

    def delete_ingredient(self, mod_sandwich):
        """Controlo las funcionalidades de eliminar ingredietes de sandwiches"""
        sandwich_ingredient = mod_sandwich.get_ingredient()
        ingredient_options = self.model.generate_available_ingredients_dict()
        finals = {}
        for ing in ingredient_options:
            if ingredient_options[ing] in [s.name for s in sandwich_ingredient]:
                finals[ing] = ingredient_options[ing]
        
        self.__initiate_view(DeleteIngredientView.DeleteIngredientView(finals))

        if len(finals) == 0:
            self.view.display_empty()
            self.view.display_negation_message()
            input()
            return self.modify_sandwich()

        self.view.display_options_menu()
        self.view.display_request_message()
        
        user_wish_ingredient = True
        while user_wish_ingredient:
            ingredient_selected_option = input()
            if ingredient_selected_option in finals:
                self.model.delete_ingredient_to_specific_sandwich(ingredient_selected_option, mod_sandwich)
                user_wish_ingredient = False
            elif ingredient_selected_option == '':
                user_wish_ingredient = False
            else:
                self.view.display_error_message()
                self.view.display_request_ingredient_message()
        self.view.display_result()
        self.view.display_new_modification()
        user_input = input()
        if user_input == 's':
            return self.delete_ingredient( mod_sandwich )
        else:
            return self.modify_sandwich()
                    
    def modify_size(self):
        """controla la funcionalidad de modificación de tamaño de sandwiches"""
        order = self.model.get_order()
        self.__initiate_view(ShowOrderView.ShowOrderView(order))
        while True:
            user_input = input()
            try:
                if user_input == 'v':
                    return self.modify_sandwich()
                elif int(user_input) in range(1,len(order.get_sandwiches())+1):
                    selected_sandwich = int(user_input)-1
                    
                    mod_sandwich = self.model.get_order().get_sandwiches()[selected_sandwich]
                    size_options = self.model.generate_available_sizes_dict()

                    self.__initiate_view(ModifySizeView.ModifySizeView(size_options))
                    self.change_size(mod_sandwich, size_options)
                else:
                    self.view.display_error_message()
                    self.view.display_request_message() 
            except ValueError:
                self.view.display_error_message()
                self.view.display_request_message()
            

    def change_size(self, selected_sandwich, size_options):
        """funcion auxiliar para la modificación de tamaño de sandwiches"""
        self.view.start_display()
        self.view.display_options_menu()
        self.view.display_request_message()

        user_wish_ingredient = True

        while user_wish_ingredient:
            size_selected_option = input()
            if size_selected_option in size_options:
                self.model.modify_size_to_specific_sandwich(size_selected_option, selected_sandwich)
                user_wish_ingredient = False
            elif size_selected_option == '':
                user_wish_ingredient = False
            else:
                self.view.display_error_message()
                self.view.display_request_ingredient_message()
        self.view.display_result()
        self.view.display_new_modification()
        user_input = input()
        if user_input == 's':
            return self.change_size(selected_sandwich, size_options)
        else:
            return self.modify_sandwich()

    def modify_sandwich(self):
        """Controla las funciones del menu de modificacion de orderdenes"""
        options = {'a' : 'Agregar Ingrediente','r' : 'Remover Ingrediente','m' : 'Modificar Tamaño','q' : 'Salir'}
        order = self.model.get_order()
        self.__initiate_view(ModifySandwichView.ModifySandwichView(options))
        if len(order.get_sandwiches()) == 0 :
            self.view.display_empty()
            input()
            return self.order_menu()
        else:
            self.view.display_options_menu()
            self.view.display_request_message()
            user_input = self.__read_option(options)
            if user_input == 'a':
                return self.add_ingredient()
            elif user_input == 'r':
                return self.selected_sandwich_disply()
            elif user_input == 'm':
                return self.modify_size()
            else:
                return self.order_menu()
            
    def clone_sandwich(self):
        """Controla la funcionalidad de clonación de sandwiches"""
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
        """Finaliza la aplicación"""
        exit()

    def delete_sandwich(self):
        """Controla la funcionalidad de eliminar sandwiches de la orden"""
        order = self.model.get_order()
        self.__initiate_view(DeleteSandwichView.DeleteSandwichView(order))

        if not len(order.get_sandwiches()):
            self.view.display_empty()
            self.view.display_finish_message()
            input()
            return self.order_menu()

        while True:
            self.view.start_display()                

            self.view.display_order()   
            self.view.display_request_message()
            
            opcion = input()
            if opcion == 'q':
                return self.order_menu()

            try:
                if int(opcion) in range(1,len(order.get_sandwiches())+1):
                    order.remove_sandwich(int(opcion))
                    self.view.display_success_message()
                    self.view.display_delete_other_confirmation()
                    final_option = input().lower()
                    if final_option == 's':
                        return self.delete_sandwich()
                    else:
                        return self.order_menu()
                else:
                    self.view.display_error_message()
            except ValueError:
                self.view.display_error_message()
            self.view.display_continue_message()
            input()

    def payment(self):
        """Controla la funcionalidad asociada al pago de la orden"""
        order = self.model.get_order()
        self.__initiate_view(PaymentView.PaymentView(order))
        if order.get_number_of_sandwiches():
            self.view.display_factura()
            self.view.display_payment_confirmation()
            opcion = input().lower()
            if opcion == 's':
                self.view.display_success_payment()
                self.model.reset_order()
                self.view.display_finish_message()
                input()
                return self.welcome()
            else:
                return self.order_menu()  
        else:
            self.view.order_empty()
            self.view.display_finish_message()
            input()
            return self.order_menu()
