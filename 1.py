class Animal:
    def __init__(self,especie,edad,genero):
        self.especie=especie
        self.edad=edad
        self.genero=genero
    def hacer_ruido(self):
        print(f"El {self.especie} esta haciendo ruido")
    def mostrar_info(self):
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.especie}")
        print(f"Genero{self.genero}")
    def dormir(self):
        print(f"El {self.especie} esta Durmiendo")
animal1= Animal("perro",5,"macho")
animal2= Animal("gato",3,"hembra")

animal1.hacer_ruido()
print("-------------------------")

animal1.mostrar_info()
animal1.dormir()

print("------------------------")

animal2.hacer_ruido()
animal2.mostrar_info()
animal2.dormir()