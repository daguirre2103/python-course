from io import open
import pathlib
import shutil

#OPEN FILE

"""
ruta = str(pathlib.Path().absolute()) + "/fichero.txt"
file = open(ruta, "a+")
"""

#WRITE FILE

#file.write("###### TEST ########\n")

#CLOSE FILE

#file.close()

#READ FILE

"""
ruta = str(pathlib.Path().absolute()) + "/fichero.txt"
file_read = open(ruta, "r")
contenido = file_read.read()
print(contenido)
"""

#READ FILE AND SAVE IN A LIST

"""
lista = file_read.readlines()
file_read.close()
"""

#READ A LIST WITH A "FOR" AND SHOW THE CONTENT

"""
for frase in lista:
    print(f"-" + frase)
"""
#READ A LIST WITH A "FOR" AND CREATE A LIST WITH EACH LINE WITH "SPLIT"

"""
for frase in lista:
    lista2 = frase.split()
    print(lista2)


for frase in lista:
    print(f"-" + frase.capitalize())
"""

#HOW TO COPY A FILE

"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero.txt"
ruta_copiada =  str(pathlib.Path().absolute()) + "/fichero2.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../07 - EJERCICIOS/fichero3.txt"

shutil.copyfile(ruta_original, ruta_copiada)
shutil.copyfile(ruta_original, ruta_alternativa)
"""

#HOW TO MOVE A FILE

"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero.txt"
ruta_movida =  str(pathlib.Path().absolute()) + "/fichero4.txt"

shutil.move(ruta_original,ruta_movida)
"""

#HOW TO DELETE A FILE

"""
import os

ruta_original = str(pathlib.Path().absolute()) + "/fichero.txt"

os.remove(ruta_original)
"""

#VERIFIED IF A FILE EXIST

import os.path
ruta_absoluta = str(pathlib.Path().absolute()) + "/fichero.txt"
ruta_relativa = "./fichero4.txt"

if os.path.isfile(ruta_relativa):
    print("El archivo existe")
else:
    print("El archivo no existe")




