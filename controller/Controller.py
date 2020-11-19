from model.Model import Model
from view.View import View

class Controller(object):

    def __init__(self, view : View, model : Model):
        self.view = view
        self.model = model
    
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
        self.view.display_wellcome_message()
