"""
LISTS (arrays) are collection o set of data/values behind a only name.
For you can access to theses values althrough a number index.

"""

#DEFINE LIST

peliculas = ["Batman", "Spiderman", "Superman"]

paises = list (("Argentina", "Brasil",'Uruguay'))

years = list(range(2023, 2040))

variados = ["David", 41, 1.77, "Flavia"]

#SHOW LISTS

"""
print(peliculas)
print(paises)
print(years)
print(variados)


#INDEX

print(peliculas[0])
print(peliculas[-2])
print(peliculas[1:3])
print(peliculas[0:])

peliculas[1] = "Flash"

print(peliculas)

#ADD ELEMENTS IN A LIST

paises.append("Bolivia")
paises.append("Chile")

print(paises)

#SEE A LIST WITH A FOR

print ("\n ########### MOVIES' LIST #################")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input ("Introduce a new movie: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

"""

#MULTIDIMENSION LIST

print("\n ########### CONTACT LIST ##################")

contactos = [

    [
        "David",
        "daguirre2103@gmail.com"
    ],
    [
        "Flavia",
        "fla.martinez.2011@gmail.com"
    ],
    [
        "Santiago",
        "santi2011@gmail.com"
    ]
]

print(contactos)
print(contactos[1][1])


# In this way I print from each list of contact the element 0(name)
for contacto in contactos:
    print(f"El nombre es: {contacto[0]}")

# In this way I print each element from each list of the big list.
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n") 








