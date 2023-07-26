paises = ["Argentina", "Brasil", "Paraguay", "Uruguay"]
numeros = [1, 2, 5, 6, 4, 8]

#Orden
print(numeros)
numeros.sort()
print(numeros)


#Add elements
print(paises)
paises.append("Chile")
print(paises)
paises.insert(2, "Bolivia")
print(paises)

#Delete elements
paises.pop(5)
print(paises)
paises.remove("Bolivia")
print(paises)

#Invert list
print(numeros)
numeros.reverse()
print(numeros)

#Count elements
print(paises)
print(len(paises))

#How many times does an element appear in the list?
numeros.append(8)
print(numeros.count(8))

#Get index
print(paises.index("Argentina"))

#Join two list
paises.extend(numeros)
print(paises)

