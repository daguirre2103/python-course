# Conditionals 

"""
if conditions;
    instructions
else:
    others intructios

"""

#Example 1:

print ("############### EXAMPLE 1 ###################3")

color = "verde"
#color = input ("Adivina mi color favorito: ")

if color == "verde":
    print ("El color es verde")
else:
    print ("El color incorrecto")
    

# Operators

"""
== igual
!= diferente
< menor que
> mayour que
<= menor o igual que
>= mayour o igua que

"""

# Example 2: if anidados

print ("\n############### EXAMPLE 2 ###################")

nombre = "David Aguirre"
ciudad = "Castelar"
continente = "Sudamerica"
edad = 41
mayoria_edad = 18

if edad >= mayoria_edad:
    print (f"{nombre} es mayor de edad")
    if continente == "Sudamerica":
        print (f"El usuario es sudamenrico y de la ciudad de {ciudad}")
    else:
        print ("El usuario no es sudamericano")
else:
    print ("No es mayor de edad")

# Elif

print ("\n############### EXAMPLE 3 ###################")

#dia = int(input("Introduce un numero de dia por favor: "))
dia = 2

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print ("Es martes")
elif dia == 3:
    print ("Es miercoles")
elif dia == 4:
    print ("Es jueves")
elif dia == 5:
    print ("Es viernes")
elif dia == 6:
    print ("Es sabado")
elif dia == 7:
    print ("Es domingo")
else:
    print("Es otra de otra semana")

# Logical operators

print ("\n############### EXAMPLE 4 ###################")

edad_minima = 18
edad_maxima = 65
edad_real = int(input("Intruduzca su edad por favor: "))

if edad_real >= edad_minima and edad_real <= edad_maxima:
    print ("Estas en edad de trabajar")
else:
    print ("No tienes edad de trabajar")

# Operator "or" is like "o" for example if pais == Arg or pais = Uruguay

# Operator "not" for example if not edad == 25

print ("\n############### EXAMPLE 5 ###################")

pais = "Colombia"

if pais == "Mexico" or "Argentina" or "Colombia":
    print ("Es un pais hispano")
else:
    print ("No es un pais Hispano")

print ("\n############### EXAMPLE 6 ###################")

pais = "Colombia"

if not (pais == "Mexico" or pais == "Argentina" or pais == "Colombia"):
    print ("NO es un pais hispano")
else:
    print ("SI es un pais Hispano")

print ("\n############### EXAMPLE 7 ###################")

pais = "Colombia"

if pais != "Mexico" and pais != "Argentina" and pais != "Colombia":
    print ("NO es un pais hispano")
else:
    print ("SI es un pais Hispano")