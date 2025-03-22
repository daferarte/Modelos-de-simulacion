################################################################
# Estructuras de control
################################################################

################################
# Condicionales
################################

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Casi eres mayor de edad")
else: 
    print("Eres menor de edad")
    
################################
# Bucles
################################

## FOR

for i in range(5):
    print(i) # imprimir los números del 0 al 4

## WHILE

contador = 0
while contador < 5:
    print(contador)
    contador += 1 # contador = contador + 1