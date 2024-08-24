
pares = [i for i in range(2, 101, 2)]
print(pares)

n_filas=10
for i in range(1, n_filas +1):
    print("*" * i)

import random    
num_ale=[random.randint(1,100) for _ in range(10)]
promedio = sum(num_ale)/len(num_ale)  
print("Arreglo de números aleatorios:", num_ale)
print("Promedio:", promedio)

 