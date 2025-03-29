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

################################
# Operadores Básicos
################################

################################
# Operadores aritméticos
################################

a = 10
b = 3

suma = a+b # 13
resta = a-b # 7
multiplicacion = a*b # 30
division = a/b # 3.333333
division_entera = a // b # 3 (division entera)
modulo = a % b # 1 (resto de la division)
exponente = a ** b # 1000 (10^3)

################################
# Operadores de comparación
################################

x = 5
y = 10

print (x > y ) # False
print (x < y ) # True
print (x == y ) # False
print (x != y ) # True

################################
# Operadores Lógicos
################################

verdadero = True
falso = False

print (verdadero and falso) # False
print (verdadero or falso) # True
print (not verdadero ) # False