import heapq

from queue import Queue

 

class Task:

    def __init__(self, id, time_arrival, age, priority, time_execution):

        self.id = id

        self.time_arrival = time_arrival

        self.age = age

        self.priority = priority

        self.time_execution = time_execution

 

    def __lt__(self, other):

        return self.priority < other.priority

 

# Cola FIFO

fifo_queue = Queue()

 

# Cola de prioridad

priority_queue = []

 

# Añadir tareas

task1 = Task(1, 0, 65, 1, 5)  # Mayor de 60 años, alta prioridad

task2 = Task(2, 1, 45, 3, 10) # Cliente regular

task3 = Task(3, 2, 70, 1, 4)  # Mayor de 60, alta prioridad

 

# Añadir a cola FIFO

fifo_queue.put(task2)

 

# Añadir a cola de prioridad

heapq.heappush(priority_queue, task1)

heapq.heappush(priority_queue, task3)

 

# Simular procesamiento

while not fifo_queue.empty():

    task = fifo_queue.get()

    print(f"Procesando tarea {task.id} desde FIFO")

 

while priority_queue:

    task = heapq.heappop(priority_queue)

    print(f"Procesando tarea {task.id} desde cola de prioridad")
    