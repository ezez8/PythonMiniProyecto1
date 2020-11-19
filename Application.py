from controller.Controller import Controller
class Application:
    def run(self):
        print('Ha iniciado la aplicacion')
        c = Controller()
        c.start()