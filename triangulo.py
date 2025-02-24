from figuras.figura import Figura

# Clase derivada Cuadrado
class Triangulo(Figura):
    def __init__(self, nombre, color,base,altura):
        super().__init__(nombre, color)
        self.base=base
        self.altura=altura
    def calcular_area(self):
        area=(self.base*self.altura)/2
        print(f"El area del {self.nombre} es de : {area}")