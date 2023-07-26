"""
A diccionary is a type of data to collect a set of values, with key-value format.
"""
#Example 1

persona = {
    "Nombre:": "David",
    "Apellido": "Aguirre",
    "Email": "daguirre2103@gmail.com"

}

print(persona)
print(persona["Apellido"])
print(persona["Nombre:"])
print(persona["Email"])

# List with a diccionary inside.

contactos = [
    {
        'Nombre': 'David',
        'Email': 'daguirre2103@gmail.com'
    },
    {
        'Nombre': 'Flavia',
        'Email': 'fla.martinez.2011@gmail.com'
    },
    {
        'Nombre': 'Santiango',
        'Email': 'santi2011@gmail.com'
    }
]

print (contactos)
print(contactos[0]["Nombre"])
contactos[1]["Email"] = "fla.martinez.2023@gmail.com"
print(contactos)

# Show the list

print("---------Contact's list----------------------------")
for contacto in contactos:
    print(f"El nombre de usuario es: {contacto['Nombre']}")
    print(f"Email de contacto: {contacto['Email']}")
    print("-------------------------------------------")

    
