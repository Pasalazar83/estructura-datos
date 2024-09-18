class Animal:
    def __init__(self, tipo, edad):
        self.tipo = tipo
        self.edad = edad

    def __str__(self):
        return f"{self.tipo} - Edad: {self.edad}"


class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar_animal(self, nuevo_animal):
        if not self.head:
            self.head = Nodo(nuevo_animal)
            return

        # Verificar si el animal ya existe
        actual = self.head
        while actual:
            if actual.animal.tipo == nuevo_animal.tipo and actual.animal.edad == nuevo_animal.edad:
                print("El animal ya está en la lista.")
                return
            if actual.siguiente is None:
                break
            actual = actual.siguiente

        actual.siguiente = Nodo(nuevo_animal)

    def mostrar_animales_recursivo(self, nodo):
        if nodo is None:
            return
        print(nodo.animal)
        self.mostrar_animales_recursivo(nodo.siguiente)

    def mostrar_animales_bucle(self):
        actual = self.head
        while actual:
            print(actual.animal)
            actual = actual.siguiente

            # Ejemplo de uso
zoologico = ListaEnlazada()
zoologico.agregar_animal(Animal("Águila", 5))
zoologico.agregar_animal(Animal("Pantera", 3))
zoologico.agregar_animal(Animal("Vaca", 2))

print("Animales en el zoológico (recursivo):")
zoologico.mostrar_animales_recursivo(zoologico.head)

print("\nAnimales en el zoológico (bucle):")
zoologico.mostrar_animales_bucle()

