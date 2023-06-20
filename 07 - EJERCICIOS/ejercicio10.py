"""
The program have to ask for fifteen test notes and show if student passed the exam or suspended it.

"""
"""
contador = 1

while contador <= 15:
    note = int(input("Introduce the exam note: "))
    if note <= 10:

        if note >= 7:
            print(f"{note} = passed")
        else:
            print(f"{note} es suspended")
    else:
        print ("Incorrect note")
    contador += 1

"""

contador = 1
aprobados = 0
suspedidos = 0

alumnos = int(input("Introduce number of students: "))
print (f"Number of students to clasificate: {alumnos}")
while contador <= alumnos:
    clasification = int(input(f"Clasification of student {contador}: "))
    if clasification >= 7:
        aprobados += 1
    else:
        suspedidos += 1
    contador += 1

print (f"Students passed: {aprobados}")
print (f"Students suspended: {suspedidos}")



         