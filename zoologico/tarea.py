# Clase Tarea
class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - Prioridad: {self.prioridad} - Vencimiento: {self.fecha_vencimiento} - Estado: {estado}"

# Clase NodoTarea
class NodoTarea:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

# Clase ListaTareas
class ListaTareas:
    def __init__(self):
        self.head = None

    def agregar_tarea(self, tarea):
        nuevo_nodo = NodoTarea(tarea)
        if not self.head or self.head.tarea.prioridad < tarea.prioridad:
            nuevo_nodo.siguiente = self.head
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente and actual.siguiente.tarea.prioridad >= tarea.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_tarea(self, descripcion):
        if not self.head:
            return
        if self.head.tarea.descripcion == descripcion:
            self.head = self.head.siguiente
            return
        actual = self.head
        while actual.siguiente:
            if actual.siguiente.tarea.descripcion == descripcion:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def mostrar_tareas(self):
        tareas = []
        actual = self.head
        while actual:
            tareas.append(actual.tarea)
            actual = actual.siguiente
        return tareas

    def completar_tarea(self, descripcion):
        actual = self.head
        while actual:
            if actual.tarea.descripcion == descripcion:
                actual.tarea.completada = True
                return
            actual = actual.siguiente

# Ejemplo de uso
gestor_tareas = ListaTareas()
gestor_tareas.agregar_tarea(Tarea("Hacer la compra", 2, "2023-10-01"))
gestor_tareas.agregar_tarea(Tarea("Estudiar para el examen", 1, "2023-09-30"))
gestor_tareas.agregar_tarea(Tarea("Lavar el coche", 3, "2023-10-15"))

print("Tareas:")
for tarea in gestor_tareas.mostrar_tareas():
    print(tarea)

gestor_tareas.completar_tarea("Estudiar para el examen")
print("\nTareas después de completar una tarea:")
for tarea in gestor_tareas.mostrar_tareas():
    print(tarea)