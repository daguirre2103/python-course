"""
Exercise 1: Make a program to have a list of 8 elements. Then do the following:
1) Loop throught the list and display it.
2) Order the list and show it.
3) Show how many elements has the list.
4) Search an element and tell me how many times does it appear?
5) Make a function to show the list.

"""

numeros = [1,3,5,4,6,8,7,4]

#Point 1

for numero in numeros:
    print(numero)

print("###################fuction:##################")

def mostrarlista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado = "\n"
        
    return resultado

print(mostrarlista(numeros))


#Point 2

print(numeros)
numeros.sort()
print(numeros)

#Point 3

print(len(numeros))

#Point 4
"""
buscar = int(input("Introduce a number: "))

if numeros.count(buscar) == 0:
    print(f"{buscar} no es exite en la lista")
else:
    print(f"El {buscar} esta {numeros.count(buscar)} veces en la lista")
"""

# Point 5

# The same exercese point 4 but with exceptions.

try:
    buscar = int(input("Introduce a number: "))

    if numeros.count(buscar) == 0:
        print(f"{buscar} no es exite en la lista")
    else:
        print(f"El {buscar} esta {numeros.count(buscar)} veces en la lista")
except:
    print("Error, ud no intrujo un numero, lo siento!")

