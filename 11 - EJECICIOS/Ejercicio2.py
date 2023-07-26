"""
Exercise 2: You have to create a list and add in it elements until the list has 20 elements. Finally you have show the list.
Plus: You must use "while" and "for".

"""
print("########## EXERCISE 2 ##############")


numeros = []

while len(numeros) <= 20:
    numero = int(input("Introduce a number please: "))
    if numero > 0:
        numeros.append(numero)
    else:
        print("Numero incorrecto")

for elemento in numeros:
    print(f"Numeros {numeros.index(elemento)}: {elemento}")

