#BUCLE WHILE

"""
estructura de control que itera o repite la ejecucion de un conjunto de instrucciones
una cantidad de veces hasta que se cumple una condicion

While condicion:
    Instracciones

"""

#EXAMPLE

contador = 1
muestrame = str(0)

while contador <= 50:
    muestrame = muestrame + ", " + str(contador)
    contador += 1
    

print(muestrame)

# EXAMPLE OF MUTIPLICATION'S TABLEw

print ("######### MULTIPLICATION'S TABLE ###########")

nro_usuario = int(input ("Please intruduce a number: "))

if nro_usuario < 1:
    nro_usuario = 1

contador = 1

while contador <= 10:
    print (f"{nro_usuario} x {contador} = {nro_usuario*contador}")
    contador += 1

print("Tabla finalizada")