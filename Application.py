from controller.Controller import Controller
class Application:
    """
    Aplicación de línea de comando, que permite a los usuarios 
    tomar órdenes de pedidos conformados por sandwiches.

    La aplicación fue implementada bajo el enfoque de programación
    orientado objetos y aplicando el patrón de diseño 
    Modelo-Vista-Controlador (MVC)

    Desarrollades:
    Bogoljubskij Hernandéz, Maximiliano
    Carbajales Di Cosola, Roberto
    Montero Pantano, Ezequiel
    Venencia Saurith, Yeisson

    """
    def run(self):
        c = Controller()
        c.start()