# main.py
from figuras.cuadrado import Cuadrado
from figuras.triangulo import Triangulo
from figuras.circulo import Circulo

from figuras.figura import Figura

# Creando objetos de cada clase derivada
figura = Figura("Escuela de figuras", "rojo")
figurac = Cuadrado("cuadrado", "verde", 5)
figurat= Triangulo ("triangulo","celeste",5,3)
figuracir = Circulo("circulo", "celeste", 15)

# Mostrando información y usando métodos
figura.mostrar_informacion()

figurac.mostrar_informacion()
figurac.calcular_area()

figurat.mostrar_informacion()
figurat.calcular_area()

figuracir.mostrar_informacion()
figuracir.calcular_area()

