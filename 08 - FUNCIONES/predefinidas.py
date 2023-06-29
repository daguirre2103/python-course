# VARIABLES

nombre = "David Aguirre"

# GENERAL FUNCTIONS

print(nombre)
print(type(nombre))

# DETECT THE TYPES

comprobar = isinstance(nombre, str)

if comprobar:
    print("Esto es un string")
else:
    print("Esto no es un string")

# CLEAR SPACES IN VARIABLES

frase = "      mi contenido       "
print(frase)
print(frase.strip())

# DELETE VARIABLES

year = 2023
print (year)
del year

# CHECK IF A VARIABLE IS EMPTY

texto = "  FF  "
if len(texto) <= 0:
    print("Variable vacia")
else:
    print("Variable no vacia", len(texto))

# FIND WORDS IN A STRING

frase = "la vida es bella"
print (frase.find("vida"))

# REPLACE WORDS IN A STRING

nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# LOWER AND UPPER WORDS

nombre = "David Aguirre"
print(nombre)
print(nombre.lower())
print(nombre.upper())




