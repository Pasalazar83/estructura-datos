class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

class metodo:
    def __init__(self):
        self.cabeza = None

    def insertar(self, datos):
        nuevo_nodo = Nodo(datos)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.datos == valor:
                return True
            actual = actual.siguiente
        return False


lista = metodo()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)

print(lista.buscar(7))  # Salida: True
print(lista.buscar(7))  # Salida: False

