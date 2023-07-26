"""
Exercise 3. You have to make a program where it has to check if a variable is empty or no. 
Finally if the variable is empty, you have fill out it in lowercase and show it in uppercase.

"""

texto = input("Introduce a word o letter: ")
if len(texto.strip()) <= 0:
    texto = "Estoy rellenando la variable"
    print (f"Texto en minuscula: {texto.lower()}")
    print (f"Texto en mayuscula: {texto.upper()}")
else:
    print(f"Texto en mayuscula: {texto.upper()}")
