"""
EXERCISE 4. You have to make a program where it create four variables (entire, string, list and boolean).
Finally you will show a text depending to type of varible.

"""

def comprobar(dato):
    if type(dato) == list:
        result = "Esta variable es una lista"
    elif type(dato) == str:
        result = "Esta variable es un string"
    elif type(dato) == int:
        result = "Esta variable es un entero"
    else:
        result = "Esta variable es un booleano"
    
    return result

my_lista = ["River", "David", "Futbol", 42]
texto = "daguirre2103"
numero = 42
verdadero = True

print(comprobar(my_lista))
