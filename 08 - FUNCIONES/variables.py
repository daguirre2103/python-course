"""
GLOBAL VARIABLES: These variables are those that can be creted outside a function and can be invocate in all code.

LOCAL VARIABLES: these variables are those created inside a function and only there can be incocate.

"""

# EXAMPLE

# GLOBAL VARIALBES

frase = "Hola mundo del voley, buenos dias"
print (frase)

def holamundo2():
    # LOCAL VARIALES
    frase = "Hola mundo del futbol, buenos dias"
    print ("Dentro de la funcion:")
    print (frase)

    # GLOBAL VARIABLE IS DEFINED INSIDE FUNCTION.
    global nombre

    nombre = "David Gaston Aguirre"
    print("Dentro: ", nombre)

    year = 2023

    return "Este es el: " + str(year)

print (holamundo2())
print("FUERA: ", nombre)

