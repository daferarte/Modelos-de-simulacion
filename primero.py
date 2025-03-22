nombre = "Juan" # Tipo str (cadena de caracteres)
edad = 25 # Tipo int(entero)
altura = 1.75 # Tipo float(decimal)
es_estudiante = True # Tipo bool (booleano => True or False)

################################
# Conocer el tipo de variable
################################

print(type(nombre)) # <class 'str'>
print(type(edad)) # <class 'int'>
print(type(altura)) # <class 'float'>
print(type(es_estudiante)) # <class 'bool'>

################################
# Conversion de tipo
################################

numero = "10"
numero_entero = int(numero) # Convierto a entero
numero_flotante = float(numero) # Conversion a flotante
print(numero_entero, numero_flotante)

