class Auto:
    # Constructor (__init__) para inicializar las propiedades
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    # Método para mostrar la información del auto
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")

    # Método para arrancar el auto
    def arrancar(self):
        print(f"El auto {self.marca} {self.modelo} ha arrancado.")

    # Método para detener el auto
    def detener(self):
        print(f"El auto {self.marca} {self.modelo} ha detenido.")

# Crear objetos de la clase Auto
auto1 = Auto("Toyota", "Corolla", 2020)
auto2 = Auto("Ford", "Mustang", 2021)

# Usar los métodos de los objetos
auto1.mostrar_info()
auto1.arrancar()
auto1.detener()

print()  # Separador entre autos

auto2.mostrar_info()
auto2.arrancar()
auto2.detener()