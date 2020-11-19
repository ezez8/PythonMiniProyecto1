from abc import ABC, abstractmethod
class View(ABC):
    def __init__(self, options : dict):
        self.options = options

    @abstractmethod
    def display_main_message(self):
        pass
    
    @abstractmethod
    def display_request_message(self):
        pass

    @abstractmethod
    def display_error_message(self):
        pass
    
    def display_options_menu(self):
        for command,option in self.options.items():
            print(f'( {command} )    {option}')
    
    def start_display(self):
        self.display_main_message()
        self.display_options_menu()
        self.display_request_message()

    def clean_screen(self):
        pass

        