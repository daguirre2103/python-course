"""
# FOR

For variable in iterable_element (For example: list, array, dictionary)
   INSTRUCTIONS BLOCK

Until the iterable element has a element the for bucle is executed

"""

#EXAMPLE 1

contador = 0
resultado = 0

for contador in range(0,5):
    print ("Voy por el numero " + str(contador))
    resultado += contador

print (f"La suman de nuestro for es: {resultado}")

# MULTIPLICATION TABLE'S EXAMPLE

numero_usuario = int(input ("Introduce el nro que quieres la tabla: "))

if numero_usuario < 1:
    numero_usuario = 1

for numero_tabla in range (1, 11):
    if numero_usuario == 45:
        print("Numero prohibido")
        break
    
    print (f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Calculo finalizado.")