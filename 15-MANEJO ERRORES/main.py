#Captch errors and exceptions in susceptible code to fails or errors
"""
try:
    nombre = input("Intruduce tu nombre por favor:")

    if len(nombre) > 1:
        nombre2 = "Su nombre es:" + nombre

    print(nombre2)
except:
    print("El nombre tiene un error, por favor corrijalo")
else:
    print("Ud introdujo un nombre correcto")
finally:
    print("script correcto")
"""

#Mutiple exceptions

"""
try:
    numero = int(input("Intruducir un numero y obtener su cuadrado:"))

    print(f"el cuadrado de {numero} es: {numero*numero}")
except TypeError:
    print("Convierta en numero a entero por favor")
except ValueError:
    print("Intrujo un numero erroneo, lo siento!")

"""

#Custom exceptions

'''
try y except:

try se utiliza para envolver un bloque de código en el que se espera que ocurra una excepción.
except se utiliza para manejar y capturar excepciones que se produzcan dentro del bloque try.
Deberías usar try y except cuando:

Tienes un bloque de código en el que puedes anticipar que pueden ocurrir excepciones.
Quieres manejar esas excepciones de manera controlada, en lugar de permitir que el programa se bloquee si ocurre una excepción.
Ejemplo:

try:
    resultado = dividir(10, 0)  # Puede generar una excepción ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
raise:

raise se utiliza para provocar manualmente una excepción en un punto específico de tu código.
Deberías usar raise cuando:

Quieras generar una excepción personalizada o lanzar una excepción específica en respuesta a una condición particular que consideres un error.
Quieras propagar una excepción que no puedes manejar en ese momento, lo que permite a un manejador de excepciones superior atraparla y gestionarla.
Ejemplo:

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return edad

try:
    edad = validar_edad(-5)
except ValueError as e:
    print(f"Error: {e}")

En resumen, try y except se utilizan para manejar excepciones que pueden ocurrir en un bloque de código específico, mientras que raise se utiliza para 
enerar excepciones manualmente cuando se necesita controlar y señalar un error en tu código. Ambas técnicas son importantes para escribir código robusto 
y resistente a errores en Python.
'''
# Example: Raise

'''
nombre = input("Introduzca un nombre: ")
edad = int(input("Introduzca una edad: "))

if edad < 5 or edad > 110:
    raise ValueError("Ud introdujo una edad errornea")
elif len(nombre) <= 1:
    raise ValueError("Introdujo un nombre erroneo")
else:
    print(f"Bienvenido al Master de python {nombre}")
'''

# Example Try except

'''
try:
    nombre = input("Introduzca un nombre: ")
    edad = int(input("Introduzca una edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("Ud introdujo una edad errornea")
    elif len(nombre) <= 1:
        raise ValueError("Introdujo un nombre erroneo")
    else:
        print(f"Bienvenido al Master de python {nombre}")
except Exception as e:
    print("Ha ocurrido el siguiente error", e)
'''


