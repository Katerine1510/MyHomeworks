# Clase base
class Figura:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    def mostrar_informacion(self):
        print(f"la figura es un : {self.nombre}")
        print(f"La figura es de color: {self.color}")
    def encender(self):
        print(f"El {self.__class__.__name__} está encendido.")