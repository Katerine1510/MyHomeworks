from figuras.figura import Figura

# Clase derivada Cuadrado
class Circulo(Figura):
    def __init__(self, nombre, color,radio,):
        super().__init__(nombre, color)
        self.radio=radio
    def calcular_area(self):
        area=3.14*self.radio**2
        print(f"El area del {self.nombre} es de : {area}")