################################################################
# Numeros aleatorios
################################################################

################################
# importando random y numpy
################################

import random
# import numpy as np

################################
# numeros pseudoaleatorios
################################

for _ in range(10):
    print(random.random())
    
################################
# numeros enteros aleatorios
################################

numero_aleatorio = random.randint(0, 10) # entero aleatorio entre 0 y 10
print(numero_aleatorio)

################################
# numeros aleatorios rango
################################

for _ in range(10):
    print(random.uniform(10, 20))

################################
# numeros aleatorios rango
################################

# aletorios = np.random.rand(5) # Arreglo de 5 numeros aleatorios entre 0 y 1
# print(aletorios)

################################
# matrices aleatorios rango
################################

# matriz_aleatoria = np.random.rand(3, 3) # Matriz de 3x3 numeros aleatorios entre 0 y 1
# print(matriz_aleatoria)