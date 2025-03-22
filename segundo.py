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
    
################################################################
# Listas y tuplas
################################################################

################################
# Lista (Mutables)
################################

frutas = ["manzana", "banana", "cereza"]
frutas.append("uva") # agregar un elemento al final
print(frutas[0]) # acceder al primer elemento
print(len(frutas)) #longitud de la lista

################################
# Tuplas (Inmutables)
################################

colores = ("rojo", "Verde", "azul")
print(colores[1])

################################################################
# Diccionarios
################################################################

persona = {
    "nombre":"Juan",
    "edad": 30,
    "ciudad": "Pasto"
}

print(persona["nombre"]) # Juan

