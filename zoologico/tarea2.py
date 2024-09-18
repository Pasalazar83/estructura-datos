class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - Prioridad: {self.prioridad} - Vencimiento: {self.fecha_vencimiento} - Estado: {estado}"


class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        self.tareas.sort(key=lambda x: x.prioridad)

    def eliminar_tarea(self, descripcion):
        self.tareas = [tarea for tarea in self.tareas if tarea.descripcion != descripcion]

    def mostrar_tareas(self):
        for tarea in self.tareas:
            print(tarea)

    def buscar_tarea(self, descripcion):
        for tarea in self.tareas:
            if tarea.descripcion == descripcion:
                return tarea
        return None

    def marcar_completada(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        if tarea:
            tarea.completada = True


# Ejemplo de uso
gestor_tareas = ListaTareas()
gestor_tareas.agregar_tarea(Tarea("Hacer la compra", 2, "2023-10-01"))
gestor_tareas.agregar_tarea(Tarea("Estudiar para el examen", 1, "2023-09-30"))
gestor_tareas.agregar_tarea(Tarea("Lavar el coche", 3, "2023-10-15"))

print("Tareas:")
gestor_tareas.mostrar_tareas()

gestor_tareas.marcar_completada("Estudiar para el examen")
print("\nTareas después de marcar una como completada:")
gestor_tareas.mostrar_tareas()