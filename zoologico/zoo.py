class Animal:
    def __init__(self, especie: str, categoria: str, edad: int):
        self.especie = especie
        self.categoria = categoria
        self.edad = edad

    def __str__(self):
        return f"{self.especie} - Categoria: {self.categoria}, Edad: {self.edad}"


class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None


class listaenlazada:
    def __init__(self):
        self.head = None

    def agregar_animal(self, nuevo_animal):
        if not self.head:
            self.head = Nodo(nuevo_animal)
            return

        actual = self.head
        while actual:
            if actual.animal.especie == nuevo_animal.especie and actual.animal.edad == nuevo_animal.edad:
                print("el animal se encuentra en la lista")
                return
            if actual.siguiente == None:
                break
            actual = actual.siguiente

        actual.siguiente = Nodo(nuevo_animal)

    def mostrar__animales__lista2(self):
        actual = self.head
        while actual:
            print(actual.animal)
            actual = actual.siguiente


zoo = listaenlazada()
zoo.agregar_animal(Animal("cocodrilo", "reptiles", 7))
zoo.agregar_animal(Animal("aguila", "aves", 30))
zoo.agregar_animal(Animal("orangutan", "primates", 18))

print("Animales en el zoologico (lista):")
zoo.mostrar__animales__lista2()