from figuras.figura import Figura

# Clase derivada Cuadrado
class Cuadrado(Figura):
    def __init__(self, nombre, color,lado):
        super().__init__(nombre, color)
        self.lado=lado
    def calcular_area(self):
        area=self.lado**2
        print(f"El area del {self.nombre} es de : {area}")



