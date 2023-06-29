"""
A function is a set of instructions grouped together with a name that it can be invocate every times you believe necesary.

def nameOfMyFunction (parameters):
    BLOCK OF INSTRUCTIONS

"""

# EXAMPLE 1

# print ("######## EXAMPLE 1 ##########")

# Create function

def mostrar ():
    print ("Flavia")
    print ("David")
    print ("Santiago")
    print ("Mateo")

# Invocate function

# mostrar ()

# EXAMPLE 2

"""
print ("######## EXAMPLE 2 ##########")


#Define function
def TuNombre (nombre, edad):
    print (f"Your name is {nombre}")
    if edad >= 18:
        print ("And you are adult")


nombre = input ("Introduce your name: ")
edad = int(input("Introduce your age: "))
#Invocate function
TuNombre(nombre, edad)

"""

# EXAMPLE 3

"""
print ("######## EXAMPLE 3 ##########")

def tabla (numero):
    print (f"Tabla de multiplicacion de: {numero}")
    for contador in range (1,11):
        operacion = numero*contador
        print (f"{numero} x {contador} = {operacion}")
    
        print ("\n")

tabla (int(input("Introduce a number: ")))

print ("#######################################")

for numero_tabla in range (1, 11):
    tabla(numero_tabla)

"""

# EXAMPLE 4
# OPTIONAL PARAMETERS

print ("######## EXAMPLE 4 ##########")

def getEmpleado (nombre, dni = None): # dni is optional
    print ("EMPLEADO")
    print (nombre)

    if dni != None:
        print (dni)

getEmpleado("David Aguirre", 29042523)
getEmpleado ("Flavia Martinez")

# EXAMPLE 5
# COMMAND RETURN

print ("#\n####### EXAMPLE 5 ##########")

def saludame (nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print (saludame ("David Aguirre"))

# EXAMPLE 6
# COMMAND RETURN

print ("\n######## EXAMPLE 6 ##########")

def calculadora (numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "La suama es:" + str(suma)
        cadena += "\n"
        cadena += "La resta es:" + str(resta)
        cadena += "\n"
    else:
        cadena += "La multiplicacion es:" + str(multi)
        cadena += "\n"
        cadena += "La division es:" + str(division)
        cadena += "\n"

    return cadena

print(calculadora(7,8, True))

# EXAMPLE 7
# FUNCTION INSIDE TO OTHER FUNCTION.

print ("\n######## EXAMPLE 7 ##########")

def getNombre (nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido (apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def getTodo (nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(getTodo("David", "Aguirre"))

# EXAMPLE 8
# LAMBDA FUNCTION.

print ("\n######## EXAMPLE 8 ##########")

dime_year = lambda year: f"The year is: {year}"

print(dime_year(2024))

















               

