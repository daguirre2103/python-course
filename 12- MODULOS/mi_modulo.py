def HolaMundo(nombre):
    return f"Hola como estas {nombre}"

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