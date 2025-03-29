################################################################
# Distribucion normal
################################################################

################################
# importando random y math
################################
import random
import math

################################
# generacion de numeros aleatorios con distribucion exponencial
################################
def generar_exponencial(lambd):
    u=random.random()
    return -math.log(1 - u) / lambd

################################
# generacion de numeros aleatorios con distribucion normal
################################
def generar_normal(mu, sigma): 
    u1 = random.random()
    u2 = random.random()
    z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    z2 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    
    return mu + sigma * z1 # o z2, ambos son numeros aleatorios nirmales independientes

# Ejemplo de uso

lambd = 0.5
mu = 0
sigma = 1

print ("Numeros aleatorios con distribucion exponencial: ")
for _ in range(10):
    print (generar_exponencial(lambd))
    
print ("Numeros aleatorios con distribucion normal: ")
for _ in range(10):
    print (generar_normal(mu, sigma))
        