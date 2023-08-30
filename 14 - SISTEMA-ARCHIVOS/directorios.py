#HOW TO CREATE A DIRECTORY

import os
import shutil

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Esta carpeta ya existe")

#HOW TO DELETE A DIRECTORY

"""
os.rmdir("./mi_carpeta")
print("Direcorio eliminado")
"""

#HOW TO COPY A DIRECTORY

"""
carpeta_original = "./mi_carpeta"
carpeta_copiada = "./mi_carpeta_copiada"

shutil.copytree(carpeta_original,carpeta_copiada)
print ("Carpeta copiada exitosamente")
"""

#HOW TO LIST THE FOLDER'S CONTENT

contenido = os.listdir("./mi_carpeta")
print(contenido)

for lista in contenido:
    print("fichero: " + lista)

